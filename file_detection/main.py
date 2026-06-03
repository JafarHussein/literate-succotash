import os
#Relative file paths
file_path="test.txt"
if os.path.exists(file_path):
    print("The file is there")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir():
        print("That is a directory")
else:
    print("I can't find that file")