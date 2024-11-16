import os
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Folder
from .serializers import FolderSerializer
from pathlib import Path
# Create your views here.

def index(request):
    file_path = os.path.join(Path(__file__).resolve().parent,'templates','index.html') 
    with open(file_path, 'r') as file: 
        file_content = file.read()
    return HttpResponse(file_content)

class FolderView(APIView):
    
    def get(self, request):
        folders = Folder.objects.filter(parent_id=None)
        serialized_folder = FolderSerializer(folders, many=True)
        return Response(serialized_folder.data)
