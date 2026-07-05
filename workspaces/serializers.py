from rest_framework import serializers
from .models import Workspace, WorkspaceMember


class WorkspaceSerializer(serializers.ModelSerializer):

    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = "__all__"

    def get_member_count(self, obj):
        return obj.members.count()
    
class WorkspaceMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkspaceMember
        fields = "__all__"

    def validate(self, attrs):

        if WorkspaceMember.objects.filter(
            workspace=attrs["workspace"],
            user=attrs["user"]
        ).exists():

            raise serializers.ValidationError(
                "User already exists in this workspace."
            )

        return attrs