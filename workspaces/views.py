from django.db import IntegrityError, transaction
from django.db.models import Count
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Workspace, WorkspaceMember, WorkspaceMemberRole
from .serializers import WorkspaceSerializer, WorkspaceMemberSerializer
from auditlogs.models import AuditLog


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = (
        Workspace.objects
        .select_related("owner")
        .annotate(member_total=Count("members"))
    )

    serializer_class = WorkspaceSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            workspace = serializer.save()

            WorkspaceMember.objects.create(
                workspace=workspace,
                user=workspace.owner,
                role=WorkspaceMemberRole.ADMIN
            )

            AuditLog.objects.create(
                actor=workspace.owner,
                action="created",
                model_name="Workspace",
                object_id=str(workspace.id)
            )

    @action(detail=True, methods=["post"])
    def members(self, request, pk=None):

        workspace = self.get_object()

        serializer = WorkspaceMemberSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        try:

            WorkspaceMember.objects.create(
                workspace=workspace,
                user=serializer.validated_data["user"],
                role=serializer.validated_data["role"]
            )

            return Response(
                {"message": "Member added."},
                status=status.HTTP_201_CREATED
            )

        except IntegrityError:

            return Response(
                {"error": "User already exists in this workspace."},
                status=status.HTTP_409_CONFLICT
            )

    @members.mapping.get
    def list_members(self, request, pk=None):

        workspace = self.get_object()

        members = WorkspaceMember.objects.filter(
            workspace=workspace
        ).select_related("user")

        serializer = WorkspaceMemberSerializer(
            members,
            many=True
        )

        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def summary(self, request, pk=None):

        workspace = self.get_object()

        return Response({

            "workspace": workspace.name,
            "documents": workspace.documents.count(),
            "members": workspace.members.count()

        })