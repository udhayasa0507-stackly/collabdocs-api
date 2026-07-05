from django.contrib import admin
from .models import Document, DocumentVersion

admin.site.register(Document)
admin.site.register(DocumentVersion)