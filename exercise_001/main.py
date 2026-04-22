# Validate user input
#1. username is no more than 12 characters
#2. username must not contain any spaces
#3. username must not contain digits

username=input("What is your username: ")

while  len(username)<=0:
    print("Your username cannot be empty")
    username=input("Please provide a valid username: ")
    
while len(username) < 12:
    print("Your username is too short,your username should be at least 12 characters")
    username=input("Please provide a valid username: ")
    
while len(username) > 12:
    print("Your username is too long,your username should be at least 12 characters")
    username=input("Please provide a valid username: ")
    
while username.isalpha() == False:
    print("Your username cannot contain any spaces or digits")
    username=input("Please provide a valid username: ")
    
print(f"Welcome to the server {username}")