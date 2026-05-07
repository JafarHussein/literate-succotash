# List comprehension= A concise way to create lists in py, compact and easier to read than traditional loops
#[expression for value in iterable if condition]

numbers=[]

for counter in range(1,11):
    numbers.append(counter * 2)
    
print(numbers)
#List comprehension
triples=[counter * 3 for counter in range(1,11)]
print(triples)

import math
squares=[math.pow(counter,2) for counter in range (1,11)]
print(squares)

#Working with strings
fruits=["Apples","Bananas","Coconut"]
uppercase_fruits=[fruit.upper() for fruit in fruits]
print(uppercase_fruits)

#Introducing conditions in the list comprehension
random_numbers=[1,2,3,4,5,-1,-2,-3,-4,-5]
positive_numbers=[number for number in random_numbers if number >=0]
print(positive_numbers)

negative_numbers=[number for number in random_numbers if number<0]
print(negative_numbers)

even_numbers=[ number for number in random_numbers if number % 2 == 0]
print(even_numbers)

odd_numbers=[number for number in random_numbers if number % 2 != 0]
print(odd_numbers)

grades=[90,80,45,32,17,56,33,44,56,67]
passing_grade=[grade for grade in grades if grade>=60]
print(passing_grade)