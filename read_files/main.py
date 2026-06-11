# lets create a plain text file and then read from it

#This is the actual file path
file_path='test.txt'

text_data='This is the actual content we are going to read when we read the test.txt file'

try:
    with open(file_path, 'w') as file:
        file.write(text_data)
        print("The write operation was succeful")
except TypeError:
    print("incompatible types, the operation failed")
    
    
#Lets read the plain text file we just created

try:
    with open(file_path,'r') as file:
       read_content=file.read()
       print(read_content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read this file")
    
    
#Lets create a json file and then read from it
import json

json_path='employee.json'
employee_dict={
    "Name":"Spongebob",
    "Age":25,
    "Job-Title":"Fry-Cook"
}

try:
    with open(json_path,'w') as file:
        json.dump(employee_dict, file, indent=4)
        print("We succefully completed the operation")
        
except TypeError:
    print("incompatible matches, the operation failed")
    
#lets read from the json file we just created
try:
    with open(json_path,'r') as file:
        json_content=json.load(file)
        print(json_content)
        print("We succefully read from the json file")
except FileNotFoundError:
    print("We could not find the stated file")
    
except PermissionError:
    print("You don't not have permission to read from the stated file")
    
    
#Lets create a csv file and then read from it

import csv

student_data=[["Name","Job-Title","Salary"],
              ["Spongebob","Fry Cook",27000],
              ["Patrick","Unemployed",0],
              ["Sandy","Scientist",150000]]

#This is the actual file path

csv_path='student_data.csv'

try:
    with open(csv_path, 'w') as file:
        writer=csv.writer(file)
        for row in student_data:
            writer.writerow(row)
        print("The write operation was succeful")
        
except TypeError:
    print("Incompatible matches, the operation failed")
    
    
#Lets read from the csv file we just created

try:
    with open(csv_path,'r') as file:
        content=csv.reader(file)
        for row in content:
            print(row)
        print("The read operation was succeful")
except FileNotFoundError:
    print("We could not locate the stated file, operation failed")
            

        
    
    

    
    

    

    