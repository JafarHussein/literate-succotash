#Conditional expressions= A one line short cut for the if-else statement, print or assign
#                         one of two values based on a condition
#                          X if condition else Y

# Sample programme

num=5

print("Positive" if num>=0 else "Negative")

# A sample programme to check if the number is even or odd

random_number=65
result="Even" if random_number % 2 == 0 else "Odd"
print(f"{random_number}",result)

#Finding the the maximum and minimum number
a=7
b=8
max_number= a if a>b else b
min_number=b if b<a else a

print(max_number)
print(min_number)

#Determining if the weather is hot or cold

temperature=20
weather="HOT" if temperature>=25 else "COLD"
print(weather)

#Determining if a person is an adult or a child
age=14
status="Adult" if age>=18 else "Child"
print(status)

