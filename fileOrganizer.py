import os

#Aim of the project
print("This program tidies up files in a specified directory by organizing them into folders based on their file type/extensions.")
path = input("Please enter the path of the directory: ")

mapping = { 'pdf': 'PDFs', 'jpg': 'Images', 'png': 'Images', 'py': 'Python', 'c' : 'C code'}

if os.path.exists(path) == True:
    #Looping the files of the path
    for root, dirs, files in os.walk(path):
        for _file in files:
            print(_file)
            extension = _file.split(".")
            print(extension[1])
else:
    print("Nope")