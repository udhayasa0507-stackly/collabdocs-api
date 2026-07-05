from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Document
from auditlogs.models import AuditLog


@receiver(post_save, sender=Document)
def create_document_audit(sender, instance, created, **kwargs):
    """
    Automatically create an AuditLog whenever
    a document is created or updated.
    """

    AuditLog.objects.create(
        actor=instance.created_by,
        action="created" if created else "updated",
        model_name="Document",
        object_id=str(instance.id)
    )