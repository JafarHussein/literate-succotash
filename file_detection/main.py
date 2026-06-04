# Detecting a file in py
import os

file_path='file_detection\test.txt'

if os.path.exists(file_path):
    print("The file exists")
elif os.path.isdir(file_path):
    print("This is a directory")

#You need to this programme in the current directory


