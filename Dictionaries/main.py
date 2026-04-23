# Dictionaries
student={
    'full_name':'Spongebob Squarepants',
    'age':25,
    'Courses':['Mathematics','Compsci']
}
#Getting the value of one key
print(student['full_name'])
print(student['courses'])
print(student['age'])

#Trying to access a key using the .get() method
print(student.get('full_name'))

#If a person tries to get acess the key that doesn't exit
print(student.get('courses','Not found'))

#Adding a new key value pair
student['Phone_number']='1234-5678-0912'
print(student)

#Updating values using the .update() method
student.update({'address':'Nairobi, Kenya'})
#The update method can be used to update existing key value pairs or adding new ones

#Deleting a property
# del student['age']

#Removing a value using .pop('key')

student_age=student.pop('age')

#Looping through all the values of a dictionary

#.keys()->This returns all the keys available in the dictionary
#.values()->This returns all the values available in the dictionary
#.items()->This returns key value pairs

for key, value in student.items():
    print(key, value)

