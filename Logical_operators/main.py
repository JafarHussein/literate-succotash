# Logicalv operators are used in conditional statements

#          and-Evaluate if two conditions are both true
#          or-Evaluate if at least one condition is true from a set
#          not-True if condition is false, vice versa


# A sample 'and' Programme

user_age=int(input("How old are you?: "))
nationality=input("Whats is your nationality?: ").lower()

if user_age>=18 and nationality == 'kenyan':
    print("You have voting rights in kenya")
else:
    print("You cannot vote in Kenya")
    
#For this programme, you need to be 18 and kenyan inorder to have voting rights



#A sample 'or' programme


english_score=float(input("What was your score in the english test: "))
kiswahili_score=float(input("What did you score in your Kiswahili test: "))
mathematics_score=float(input("What did you score in your mathematics exams: "))


if mathematics_score>=70 and mathematics_score<=100:
    if kiswahili_score or english_score >=70 and kiswahili_score or english_score <=100:
        print("You are eligible for the law course in campus")
    else:
        print("You are not eligible for the law course")
    print("*********************************************")
    
    
#A sample 'not' programme 

is_light_on=True

if not is_light_on:
    print("The room is dark")
else:
    print("The room is brightly light")
    
