import os

print("This program tidies up files in a specified directory by organizing them into folders based on their file type/extensions.")
dirName = input("Please enter the path of the directory: ")

if os.path.exists(dirName) == True:
    print("YUP")
else:
    print("Nope")