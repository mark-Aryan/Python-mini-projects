import zipfile


def extract(zipFolder, path):
    with zipfile.ZipFile(zipFolder, 'r') as archive:
        archive.extractall(path=path)
