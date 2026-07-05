from rest_framework import viewsets

from .models import AuditLog
from .serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = (
        AuditLog.objects
        .select_related("actor")
    )

    serializer_class = AuditLogSerializer