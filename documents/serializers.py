from rest_framework import serializers
from .models import Document
from .models import DocumentVersion

class DocumentSerializer(serializers.ModelSerializer):

    latest_version = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = "__all__"

    def get_latest_version(self, obj):

        version = obj.versions.order_by("-version_number").first()

        if version:
            return version.version_number

        return None
    
class DocumentVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentVersion
        fields = "__all__"