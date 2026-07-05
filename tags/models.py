from django.db import models
from core.models import BaseModel
from documents.models import Document


class Tag(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    documents = models.ManyToManyField(
        Document,
        related_name="tags",
        blank=True
    )

    def __str__(self):
        return self.name