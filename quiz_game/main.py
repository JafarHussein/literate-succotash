questions=('1.Which planet is known as the red planet',
           '2. What is the chemical symbol for Gold',
           '3.Which artist painted the monalisa',
           '4. What is the capital city of australia',
           '5. How many hearts does an octopus have')

question_options=(('A. Venus', 'B. Mars', 'C. Jupiter', 'D,Saturn'),
                  ('A. Ag','B. Fe','C. Au','D. Pb'),
                  ('A. Leonardo da vinci','B. Vincent van Goh','C. Pablo picasso','D.Claude monet'),
                  ('A. Sydeny', 'B.Mellbourne','C.Canberra','D.Perth'),
                  ('A.1','B.2','C.3','D.4'))

question_answers=('B','C','A','C','C')

guesses=[]

user_input=None

question_num=0

user_score=0


for question in questions:
    print('----------------------')
    print(question)
    for option in question_options[question_num]:
        print(option)
        
    user_input=input("Choose A, B, C OR D: ").upper()
    guesses.append(user_input)
    if user_input == question_answers[question_num]:
        print("Thats correct ✅")
        user_score+=1
    else:
        print("Thats wrong ❌")
        print(f"The correct answer is {question_answers[question_num]}")
    question_num+=1
    
    
print(f"You score is {user_score}/{len(questions)}")
