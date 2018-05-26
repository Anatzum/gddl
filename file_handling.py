import rarfile
import os
import magic


def handle(file_location, directory):
    types_dict = {"RAR archive data": extract_rar}
    ftype = magic.from_file(file_location).split(',')[0]

    if ftype in types_dict:
        types_dict[ftype](file_location, directory)
    else:
        pass


def extract_rar(file_location, directory):
    with rarfile.RarFile(file_location) as rf:
        rf.extractall(path=directory)
        os.remove(file_location)
