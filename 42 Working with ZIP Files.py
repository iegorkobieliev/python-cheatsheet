import zipfile
with zipfile.ZipFile('archive.zip', 'w') as myzip:
    myzip.write('file.txt')
with zipfile.ZipFile('archive.zip', 'r') as myzip:
    myzip.extractall('extracted')