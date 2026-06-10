
#Exercise 1

#Write a python script that takes the following dictionary and saves it into a file named settings.json, make sure the resulting json file is cleanly formatted and easy for a human to read

import json

game_settings={
    "username":"ShadowNinja",
    "volume":80,
    "fullscreen":True,
    "controls":["w","A","S","D"]
}

#This is the file path
settings_json='settings.json'

try:
    with open(settings_json,'w') as file:
        json.dump(game_settings, file, indent=4)
        print("Settings succefully saved")
except TypeError:
    print("Incompatible types involved, the operation failed")
    
    
#An exercise on csv files

#Write a Python script using the built-in csv module to write the following list of data into a file named grades.csv.

import csv

student_data=[
    ['Alice','Math',95],
    ['Bob','Science',88],
    ['Charlie','History',92],
]

student_data=[['Name','Subject','Score'],
              ['Alice','Math',95],
              ['Bob','Science',88],
              ['Charlie','History',92]]

#This is file path
grades_csv='grades.csv'

try:
    with open(grades_csv,'w') as file:
        writer=csv.writer(file)
        for row in student_data:
            writer.writerow(row)
        print("The operation was succeful")
except TypeError:
    print("Incompatible types involved, the operation failed")
    
    
    
#Writing on a plain file
text_data='Secret Agent Report: The package has been successfully delivered to the safehouse at midnight.'

#Actual file path
secret_log='secret_log.txt'

with open(secret_log,'w') as file:
    for letter in text_data:
        if letter == 'e' or letter == 'E':
            continue
        else:
            file.write(letter)

    