#sample programme to determine if users are of the right age to be driving
user_age=int(input("Please provide your current age: "))
if user_age>=18 and user_age<100:
    print("You are eligible to drive")
elif user_age>100:
    print("You are too old to be driving")
else:
    print("You are too young to be driving")
    

    