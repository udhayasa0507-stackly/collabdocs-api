from django.db import models
from core.models import BaseModel
from users.models import User


class AuditLog(BaseModel):
    actor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="audit_logs"
    )

    action = models.CharField(max_length=50)

    model_name = models.CharField(max_length=100)

    object_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.action} - {self.model_name}"