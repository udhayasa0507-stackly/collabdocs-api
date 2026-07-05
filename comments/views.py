from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = (
        Comment.objects
        .select_related(
            "author",
            "document",
            "parent"
        )
    )

    serializer_class = CommentSerializer

    def get_queryset(self):

        queryset = super().get_queryset()

        document = self.request.query_params.get("document")

        if document:
            queryset = queryset.filter(document=document)

        return queryset