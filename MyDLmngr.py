import sys
import requests

def getFileInfo():
    requestedFile = requests.get(sys.argv[1])
    fileName = sys.argv[2]
    return (requestedFile, fileName)

def download():
    reqFile, name = getFileInfo()
    with open(name, 'wb') as f:
        f.write(reqFile.content)

download()
