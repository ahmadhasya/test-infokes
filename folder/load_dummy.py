from pathlib import Path
from .models import File,Folder

def run(verbose=True):
    folder = Folder(name="Folder 1")
    folder.save()
    File(name="File 1.1",parent=folder).save()
    File(name="File 1.2",parent=folder).save()
    Folder(name="Subfolder 1.1",parent=folder).save()
    sub_folder = Folder(name="Subfolder 1.2",parent=folder)
    sub_folder.save()
    Folder(name="Subfolder 1.3",parent=folder).save()
    File(name="File 1.2.1",parent=sub_folder).save()
    Folder(name="Subfolder 1.2.1",parent=sub_folder).save()
    Folder(name="Subfolder 1.2.1",parent=sub_folder).save()

    folder = Folder(name="Folder 2")
    folder.save()
    File(name="File 2.1",parent=folder).save()
    File(name="File 2.2",parent=folder).save()
    Folder(name="Subfolder 2.1",parent=folder).save()
    sub_folder = Folder(name="Subfolder 2.2",parent=folder)
    sub_folder.save()
    Folder(name="Subfolder 2.2.1",parent=sub_folder).save()
    Folder(name="Subfolder 2.2.2",parent=sub_folder).save()
    Folder(name="Subfolder 2.2.3",parent=sub_folder).save()
    sub_folder = Folder(name="Subfolder 2.3",parent=folder)
    sub_folder.save()
    File(name="File 2.2.1",parent=sub_folder).save()
    