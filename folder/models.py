from django.db import models

class Folder(models.Model):
    name = models.CharField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class File(models.Model):
    name = models.CharField()
    parent = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)