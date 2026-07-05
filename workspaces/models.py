from django.db import models
from core.models import BaseModel
from users.models import User


class WorkspaceMemberRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    EDITOR = "editor", "Editor"
    VIEWER = "viewer", "Viewer"


class Workspace(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_workspaces"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class WorkspaceMember(BaseModel):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workspace_memberships"
    )

    role = models.CharField(
        max_length=20,
        choices=WorkspaceMemberRole.choices
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["workspace", "user"],
                name="unique_workspace_member"
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.workspace.name}"