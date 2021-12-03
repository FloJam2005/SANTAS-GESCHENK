# Challange: https://www.youtube.com/watch?v=G3vLQP5yAKQ&t=18s

import zipfile
import os


path = "pfad/zum/Ordner"
# Beispiel: "D:/SantasGeschenk/"


def extract(filename):
    zip=zipfile.ZipFile(path+filename)
    zip.extractall(path+"/")
    zip.close()

def deleteFile(filename):
    os.remove(path+filename)
def isZip(filename):
    if filename.endswith(".zip"):
        return True
    else:
        return False
def istxt(filename):
    if filename.endswith(".txt"):
        datei = open(path+filename)
        print(datei.read())
        datei.close()
        return True

async def sleep():
    await asyncio.sleep(500)
x = 1
while True:
    datein=os.listdir(path+"/")
    filename = datein[0]
    print(filename)
    if istxt(filename):
      break
    if isZip(filename):
        extract(filename)

    print(f'Ebene: {x}')
    x = x+1
    deleteFile(filename)
