import rarfile
import os
import magic
import zipfile


def get_file_type(file_location):
    return magic.from_file(file_location).split(',')[0]


def is_archive(file_location):
    ftype = get_file_type(file_location)

    if ftype in archives_dict:
        return True
    else:
        return False


def extract(file_location, directory):
    archives_dict[get_file_type(file_location)](file_location, directory)


def extract_rar(file_location, directory):
    with rarfile.RarFile(file_location) as rf:
        rf.extractall(path=directory)
        os.remove(file_location)


def extract_zip(file_location, directory):
    with zipfile.ZipFile(file_location) as zf:
        zf.extractall(path=directory)
        remove_file(file_location)


def extract_tar(file_location, directory):
    pass


def remove_file(file_location):
    os.remove(file_location)


archives_dict = {"RAR archive data": extract_rar,
                 "Zip archive data": extract_zip,
                 "POSIX tar archive": extract_tar}
