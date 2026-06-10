# File detection using py
import os

# Creating a file path that leads to that file we trying to detect

file_path='test.txt'

if os.path.exists(file_path):
    print("The file exists")
else:
    print("That file doesn't exist")
    
    
#Checking if the file is a file or a directory

if os.path.isfile(file_path):
    print("This is a file")
else:
    print("This is not a file")
    

#Checking if its a directory

if os.path.isdir(file_path):
    print("This is a directory")
else:
    print("This is not a directory")