# Python quiz game
questions=('How many elements are in the periodic table?: ',
           'Which animal lays the largest eggs?: ',
           'Which is the most abundant gas in our atmosphere',
           'How many bones are in the human body: ',
           'Which planet on the solar system is the hottest: ')
options=(('A.116','B.117','C.118','D.119'),
         ('A.Whale','B.Crocodile','C.Elephant','D.Ostrich'),
         ('A.Nitrogen','B.Oxygen','C.Carbon dioxide','D.Sulphur'),
         ('A.200','B.201','C.206','D.207'),
         ('A.Mercury','B.Venus','C.Jupiter','D.Earth'))

answers=('C','D','A','C','B')
guesses=[]
question_num=0
score=0

for question in questions:
    print("**************************")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter A, B, C or D").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer is {answers[question_num]}")
    question_num+=1
    
    
print(f"Your score {score}")