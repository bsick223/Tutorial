import os

path = "/Tutorial/FirstFolder"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("that is file")
    elif os.path.isdir(path):
        print("That is a directory! ")
else:
    print("That location doesn't exist!")
