# lets build a password strength checker
import random
import string

#Variable declaration
lower_chars='abcdefghijklmnopqrstuvwxyz'
upper_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit_chars='1234567890'
symbol_chars='~!@#$%^&*()_+'
has_lower=False
has_upper=False
has_digits=False
has_symbols=False
password_score=0

#Accepting user input
print("----This is a simple py programme that checks how strong your password is ----")
user_password=input("Please enter your password: ")

if len(user_password)== 0 or user_password==' ':
    print("No feedback provided ❗")
    user_password=input("Please enter your password: ")
while len(user_password)>0:
    if len(user_password)<6:
        print(f'Your password length is {len(user_password)} characters long, thats a very weak password')
        user_passwor=input("Please provide another password: ")
    elif len(user_password)>=6 and len(user_password)<=7:
        print(f"Your password length is {len(user_password)} characters long, thats a weak password")
        user_password=input("Please provide another password")
    elif len(user_password)>=8 and len(user_password)<=15:
        print(f"Your password length is {len(user_password)} characters long, thats a strong password")
        password_score+=2
        break
    elif len(user_password)>=16:
        print(f"Your password length is {len(user_password)} characters long, thats a very strong password")
        password_score+=5
        break
        
#Check the password, lets avoid the generic stuff

if user_password == 'password':
    password_score-=1
    
if user_password =='password123':
    password_score-=1
    
if user_password == 'abcdef':
    password_score-=1
    
if user_password == '12345':
    password_score-=1
    
for letter in user_password:
    if letter in lower_chars:
        has_Lower=True
        
for letter in user_password:
    if letter in upper_chars:
        has_upper=True
        
for letter in user_password:
    if letter in digit_chars:
        has_digits=True
        
for letter in user_password:
    if letter in symbol_chars:
        has_symbols=True
                     
        
if has_lower:
    password_score+=1

if has_upper:
    password_score+=1
      
if has_digits:
    password_score+=1
    
if has_symbols:
    password_score+=1
    
    
if password_score <=2:
    print(f"Your password: {user_password}")
    print(f"Your password score: {password_score}")
    print("Thats a very weak password")
elif password_score >= 3 and password_score <= 5:
    print(f"Your password: {user_password}")
    print(f"Your password score: {password_score}")
    print("Thats moderately strong")
elif password_score > 8:
    print(f"Your password: {user_password}")
    print(f"Your password score: {password_score}")
    print("Thats a very strong password")
    
    
if password_score > 0 and password_score<=3:
    user_feedback=input("Would you like me to generate a new password(y/n): ").lower()
    if user_feedback == 'y':
        password_length=int(input("How long should the password be: "))
        chars=list(string.punctuation + string.ascii_letters + string.digits)
        new_password=''
        key=chars.copy()
        random.shuffle(key)
        for counter in range(1, password_length):
            new_password+=key[counter]
        user_password=new_password
        print("Password has been succefully generated")
        print(f"new password: {user_password}")
    else:
        print("You have a lovely day")