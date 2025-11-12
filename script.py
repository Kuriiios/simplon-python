import os 

PATH = '.venv'

Nroots = sum(len(root) for root, filenames, dirnames in os.walk(PATH))
Nfiles = sum(len(filenames) for root, filenames, dirnames in os.walk(PATH))
Ndirs = sum(len(dirnames) for root, filenames, dirnames in os.walk(PATH))

print(f"Number of roots: {Nroots}, Number of files: {Nfiles}, Number of directories: {Ndirs}")