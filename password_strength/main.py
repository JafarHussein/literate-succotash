#lets make a programme that checks how strong your password is

import string
print("This is a simple py programme that checks how strong your password")
user_password=input("Please enter your password: ")
while len(user_password) == 0:
    print("Your password cannot be empty")
    user_password=input("Please enter your password: ")
    
lower_chars="abcdefghijklmnopqrstuvwxyz"
upper_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number_chars="1234567890"
symbol_chars="~!@#$%^&*()_+<>?"
password_score=0
while len(user_password)>0:
    if len(user_password)<=6:
        print(f"Your password length is {len(user_password)}, thats a very weak password")
        user_password=input('Please enter a password that is atleast 12 characters long: ')
    elif len(user_password) > 6 and len(user_password)<=7:
        print(f"Your password length is {len(user_password)}, thats a weak password")
        user_password=input('Please enter a password that is atleast 12 characters long: ')
    elif len(user_password) > 8 and len(user_password)<=11:
        print(f"Your password length is {len(user_password)}, thats a moderately strong password")
        user_password=input('Please enter a password that is atleast 12 characters long: ')
        
if len(user_password) >=8:
    password_score+=1
        
if len(user_password)>=12:
    print("Your password length is great ✅")
    
for letter in user_password:
    if lower_chars.count(letter) > 1:
        print(f"{letter} has been repeated {lower_chars.count(letter)} times, to increase the strength of each password its better if you only used it ")  