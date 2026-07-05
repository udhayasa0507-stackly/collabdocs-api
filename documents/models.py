from django.db import models
from core.models import BaseModel
from users.models import User
from workspaces.models import Workspace


class DocumentStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"
    ARCHIVED = "archived", "Archived"


class Document(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="documents"
    )

    status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.DRAFT
    )

    def __str__(self):
        return self.title


class DocumentVersion(BaseModel):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="versions"
    )

    content = models.TextField()

    version_number = models.PositiveIntegerField()

    saved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="saved_versions"
    )

    def __str__(self):
        return f"{self.document.title} v{self.version_number}"