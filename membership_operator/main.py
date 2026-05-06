# Membership operator = used to test whether a value or a variable is found in a sequence(string, list, tuple, set or dictionary)
#1. in
#2. not in

secret_word='APPLE'

letter=input("Guess a letter that can be in the secret word: ").upper()

while letter not in secret_word:
    print(f"{letter} is not in the secret word")
    letter=input("Please try again: ")
    
students={"spongebob", "patrick", "sandy","squidward"}
print("This is a simple search engine")
student_name=input("Enter student name you looking for: ")
if student_name in students:
    print(f"{student_name} was found in the database")
else:
    print(f"{student_name} was not found in the database")

grades={"sandy":"A","spongebob":"B","patrick":"C","squidward":"D"}
student_key=input("Enter student name to see student grade: ")

if student_key in grades:
    student_grade=grades.get(student_key)
    print(f"{student_key} scored: {student_grade}")
else:
    print("The student was not found in the database")