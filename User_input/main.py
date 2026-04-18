#Asking the user for their name and then type casting it as a string
full_name=str(input("Whats your full name: "))
print(f"Hello {full_name}")

#Asking the user for their age and then type casting their age as an integer
age=int(input("How old are you: "))
if age >=18:
    print("You are an adult")
elif age<=0:
    print("You haven't been born yet")
else:
    print("You are too old")
    
#Asking if the user is still in school and then type casting it as an integer
is_student=input("Are you in school?(High school, uni, college), if you in school type (y/n)")
if is_student == 'y':
    is_student_boolean=True
else:
    is_student_boolean=False
    

print(full_name)
print(age)
print(is_student_boolean)


