import json

text_data="We writting this exact information to the a new file"
file_path='test.txt'

with open(file_path,'w') as file:
    file.write(text_data)
    print(f"txt file {file_path} was created")
    
# x- creating a file and writing to it, if the file already exists this is going to throw an error

#w-This is writing to a file, if the file doesn't exists it will create it, if the file exists it will over ride it

#a-This is used to append to files, just add on the content that already exists

#Iterating over a list and writing the  values on a file

employees=['Eugene','Squirdward','Spongebob','Patrick']

employee_file='employee.txt'

with open(employee_file,'w') as file:
    for employee in employees:
        file.write(employee + " ")
        print()
        
    print("All the employees have been added to the employee file")
    
    
employees_dict={
    "name":"Eugene",
    "age":55,
    "position":"manager"
}

employee_json='employee.json'

with open(employee_json,'w') as file:
    json.dump(employees_dict,file, indent=4)
    print("Operation was done succefully")
    
    
#working with csv files

import csv

employee_csv=[["Name","Age","Job-Title"],
              ["Spongebob",30,"Fry-cook"],
              ["Patrick",35,"Unemployed"],
              ["Sandy",27,"Scientist"]]

employee_csv_path='employees.csv'

with open('employees.csv','w', newline="") as file:
    writer=csv.writer(file)
    for row in employee_csv: 
        writer.writerow(row)
    print("CSV file was created")

    


