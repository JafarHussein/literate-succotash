# Lets a make a simple programme that checks how strong your password is 
import random
import string

#Variables
lower_chars='abcdefghijklmnopqrstuvwxyz'
upper_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number_chars='1234567890'
symbol_chars='~!@#$%^&*()_+'
has_lower=False
has_upper=False
has_symbols=False
has_digits=False
password_score=0

print("A py programme that checks how strong your password is")

#Accepting user input
user_password=input("Please enter your password: ")

while len(user_password) == 0:
    print("Your password cannot be empty")
    user_password=input("Please enter your password: ")
    
while len(user_password)>0:  
    if len(user_password)>0 and len(user_password)<6:
        print(f"Your password length is {len(user_password)}, thats a very weak password")
    elif len(user_password)>=6 and len(user_password)<=7:
        print(f"Your password length is {len(user_password)}, thats a weak password")
    elif len(user_password)>=8 and len(user_password)<=11:
        print(f"Your password length is {len(user_password)}, thats a moderately strong password")
        password_score+=1
        break
    elif len(user_password)>=12 and len(user_password)<=15:
        print(f"Your password length is {len(user_password)}, thats a  strong password")
        password_score+=2
        break
    elif len(user_password)>15:
        print(f"Your password length is {len(user_password)}, thats a very strong password ")
        password_score+=5
        break
    
#Checking what characters are in the password string
for letter in user_password:
    if letter in lower_chars:
        has_lower=True
    elif letter in upper_chars:
        has_upper=True
    elif letter in number_chars:
        has_digits=True
    elif letter in symbol_chars:
        has_symbols=True
        
        
if has_lower:
    password_score+=1

if has_upper:
    password_score+=1
    
if has_symbols:
    password_score+=1
    
if has_digits:
    password_score+=1
    
if user_password == 'password':
    password_score-=1
elif user_password == 'aaaaaaa':
    password_score-=1
elif user_password == '12345':
    password_score-=1
elif user_password == 'abcdef':
    password_score-=1
elif user_password == 'qwerty':
    password_score-=1
    
    
if password_score <=0 and password_score<=2:
    print(f"Your password score: {password_score}")
    print("Your password is very weak")
elif  password_score >=3 and password_score<=5:
    print(f"Your password score: {password_score}")
    print("Your password is weak")
elif password_score >=6 and password_score<=7:
     print(f"Your password score: {password_score}")
     print("Your password strength is medium")
elif password_score > 7:
     print(f"Your password score: {password_score}")
     print("Your password is very strong")
     
     
print(f"User password:{user_password}")
print(f"Password score: {password_score}")

user_feedback=''
if password_score < 5:
    user_feedback=input("Would you like me to generate a strong password(y/n): ").lower()
    
if user_feedback == 'y':
    password_length=int(input("How long would you like the password to be: "))
    chars=list(string.punctuation + string.ascii_letters + string.digits + " ")
    new_password=''
    random.shuffle(chars)
    for counter in range(0,password_length):
        index=random.randint(0, len(chars))
        new_password+=chars[index]
    user_password=new_password
    print("Your new strong password has been generated succefully ✅")
    print(f"new password: {user_password}")
else:
    print("Byee, have a lovely day")
        
