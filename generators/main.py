# Generators = Function that behave like iterators (it can be used in a for loop), you can pause the function, it returns a value then resumes. It used yield instead of return.It best used to read large fills
import math

# def square(unsquared_numbers):
#     results=[]
    
#     for number in unsquared_numbers:
#         results.append(math.pow(number, 2))
        
#     return results

random_numbers=[2,3,4,5,6,7]

# print(square(random_numbers))


# Turning the above function into a generator

def square(unsquared_numbers):
    for number in unsquared_numbers:
        yield(math.pow(number,2))
        
        
squared_numbers=square(random_numbers)

while True:
    try:
        print(next(squared_numbers))
    except StopIteration:
        break