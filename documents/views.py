from django.db import transaction
from django.db.models import Count, Q
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Document, DocumentVersion
from .serializers import (
    DocumentSerializer,
    DocumentVersionSerializer
)

from tags.models import Tag
from auditlogs.models import AuditLog


class DocumentViewSet(viewsets.ModelViewSet):

    serializer_class = DocumentSerializer

    queryset = (
        Document.objects
        .select_related(
            "workspace",
            "created_by"
        )
        .prefetch_related("tags")
    )

    def get_queryset(self):

        queryset = super().get_queryset()

        search = self.request.query_params.get("search")
        status_filter = self.request.query_params.get("status")

        if status_filter:
            queryset = queryset.filter(status=status_filter)

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        return queryset

    def perform_create(self, serializer):

        with transaction.atomic():

            document = serializer.save()

            version = document.versions.count() + 1

            DocumentVersion.objects.create(
                document=document,
                content=document.content,
                version_number=version,
                saved_by=document.created_by
            )

            AuditLog.objects.create(
                actor=document.created_by,
                action="created",
                model_name="Document",
                object_id=str(document.id)
            )

    def perform_update(self, serializer):

        with transaction.atomic():

            document = serializer.save()

            version = document.versions.count() + 1

            DocumentVersion.objects.create(
                document=document,
                content=document.content,
                version_number=version,
                saved_by=document.created_by
            )

            AuditLog.objects.create(
                actor=document.created_by,
                action="updated",
                model_name="Document",
                object_id=str(document.id)
            )

    @action(detail=True, methods=["get"])
    def versions(self, request, pk=None):

        document = self.get_object()

        versions = document.versions.order_by("-version_number")

        serializer = DocumentVersionSerializer(
            versions,
            many=True
        )

        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def stats(self, request, pk=None):

        document = self.get_object()

        return Response({

            "versions": document.versions.count(),

            "comments": document.comments.count(),

            "tags": document.tags.count()

        })

    @action(detail=True, methods=["post"])
    def tags(self, request, pk=None):

        document = self.get_object()

        tag_ids = request.data.get("tags", [])

        tags = Tag.objects.filter(
            id__in=tag_ids
        )

        document.tags.set(tags)

        return Response({
            "message": "Tags updated successfully."
        })