import os

source = 'folder'
destination = '/Users/brendan/Desktop/folder'

try:
    if os.path.exists(destination):
        print("there is already a file here with the same name.")
    else:
        os.replace(source, destination)
        print("file was transferred successfully.")

except FileNotFoundError:
    print("file was not found")
