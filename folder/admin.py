from django.contrib import admin
from .models import Folder,File

# Register your models here.
admin.site.register(Folder, admin.ModelAdmin)
admin.site.register(File, admin.ModelAdmin)