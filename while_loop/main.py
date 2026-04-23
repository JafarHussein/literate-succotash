# While loop will execute some condition infinetly while some condition remains true

username=input("What is username: ")
while username == '':
    print("username cannot be an empty string")
    username=input("please enter a valid username: ")
    
print(f"Welcome {username}")

random_number=int(input("Please select a random number: "))
while not random_number % 2 == 0:
    print("NO")
    random_number=int(input("Please choose another number: "))
print(random_number)

