#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This script will organize your download folder for you.
    Make sure you create a .txt file named FolderPath.txt where you write the path of your Download Folder.
"""
import os, shutil

extension_to_folder = {
    "pdf":"PDFs",
    "jpg":"Imágenes",
    "png":"Imágenes",
    "avi":"Vídeos",
    "mp4":"Vídeos",
    "docx":"Documentos",
    "txt":"Documentos",
    "zip":"Comprimidos",
    "rar":"Comprimidos",
    "mp3":"Sonidos",
    "exe":"Ejecutables"
}

def FolderPath():
    try: 
        with open("FolderPath.txt") as f:
            folder = f.readlines()
            return str(folder[0])
    except Exception as e:
        print("Folder with path didn't found: ", {e})

def main():
    folder = FolderPath()

    for file in os.listdir(folder):
        extension = os.path.splitext(file)[1][1:]
        if extension in extension_to_folder:
            try:
                file_path = os.path.join(folder, file)
                destination_path = os.path.join(folder, extension_to_folder.get(extension))

                os.makedirs(destination_path, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_path, file))

            except Exception as e:
                print("Error while creating or moving: ", {e})
        else:
            continue
    print("Su carpeta ha sido ordenada.")

if __name__ == "__main__":
    main()