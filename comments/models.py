from django.db import models
from core.models import BaseModel
from documents.models import Document
from users.models import User


class Comment(BaseModel):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments"
    )

    content = models.TextField()

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="replies"
    )

    def __str__(self):
        return self.content[:30]