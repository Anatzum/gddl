import rarfile
import os
import magic
import zipfile


def handle(file_location, directory):
    types_dict = {"RAR archive data": extract_rar,
                  "Zip archive data": extract_zip}
    ftype = magic.from_file(file_location).split(',')[0]

    if ftype in types_dict:
        types_dict[ftype](file_location, directory)
    else:
        pass


def extract_rar(file_location, directory):
    with rarfile.RarFile(file_location) as rf:
        rf.extractall(path=directory)
        os.remove(file_location)


def extract_zip(file_location, directory):
    with zipfile.ZipFile(file_location) as zf:
        zf.extractall(path=directory)
        remove_file(file_location)


def remove_file(file_location):
    os.remove(file_location)
