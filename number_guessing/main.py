# Lets make a simple number guessing game in py
import random

#This generates a random number in the specified range
random_number=random.randint(0,100)

#Accepting some input from the user
user_input=int(input("Choose a random number between 0 and 100: "))

while user_input != random_number:
    if user_input> random_number:
        print("Your guess is higher ❌")
        user_input=int(input("Please choose another random number: "))
    elif user_input< random_number:
        print("You guess is below the random number ❌")
        user_input=int(input("Please choose another number"))

print("Right guess ✅")
print(f"Random number {random_number}")
print(f"Your guess {user_input}")
        