from rest_framework import serializers
from .models import Folder,File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'parent_id', 'created_at', 'updated_at']

class FolderSerializer(serializers.ModelSerializer):
    subfolders = serializers.SerializerMethodField()
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'subfolders', 'files', 'parent_id', 'created_at', 'updated_at']

    def get_subfolders(self, obj):
        subfolder = Folder.objects.filter(parent_id=obj.id)
        if subfolder.exists():
            return FolderSerializer(subfolder, many=True).data
        return []