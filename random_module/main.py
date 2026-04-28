import random
# For a random whole integer

#random.randint(min, max)
random_integer=random.randint(1,6)
print(random_integer)

#random floating point number
floating_number=random.random()
print(floating_number)

#Choosing a random choice from a few given choices
options=('Scissors','Paper','Rock')
random_choice=random.choice(options)
print(options)


#Lets build a simple rock, paper, scissors game in py
game_options=['Rock','Paper','Scissors']
computer_score=0
user_score=0

user_choice=" "
while user_choice !="Quit":
    user_choice=input("Please choose between rock, paper and scissors: ").capitalize()
    computer_choice=random.choice(game_options)
    if user_choice == computer_choice:
        print(f"{user_choice} vs {computer_choice}")
        print("ITS A TIE")
        print(f"{computer_score}")
        print(f"{user_score}")
    elif user_choice != computer_choice:
        if user_choice == 'Rock' and computer_choice =='Paper':
            user_score+=1
            print(f"{user_choice} vs {computer_choice}")
            print("You win 🥳")
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            user_score+=1
            print(f"{user_choice} vs {computer_choice}")
            print("You win 🥳")
        elif user_choice == 'Scissors' and computer_choice =='Paper':
            user_score+=1
            print(f"{user_choice} vs {computer_choice}")
            print("You win 🥳")
        elif computer_choice == 'Paper' and user_choice =='Rock':
            computer_score+=1
            print(f"{user_choice} vs {computer_choice}")
            print("You Lose 😭")
        elif computer_choice == 'Scissors' and user_choice == 'Paper':
            computer_score+=1
            print(f"{user_choice} vs {computer_choice}")
            print("You Lose 😭")
        elif computer_choice == 'Rock' and user_choice == 'Scissors':
            computer_score+=1
            print(f"{user_choice} vs {computer_choice}")
            print("You Lose 😭")
    else:
        break
    print(f"Computer score:{computer_score} ")
    print(f"User score:{user_score} ")
    