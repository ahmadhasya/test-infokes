from django.urls import path
from . import views

urlpatterns = [
    path("all", views.FolderView.as_view(), name="folder"),
    path("", views.index, name="index"),
]