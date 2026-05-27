# An exercise to test my understanding on the concept of nested classes

#exercise 1
# 1. Create a Library class with a nested Book class. Book takes a title and author. Its __str__ should return "Dune by Herbert". Instantiate a book using Library.Book(...) and print it.
# class Library:
#     class Book:
#         def __init__(self, title, author):
#             self.title=title
#             self.author=author
            
#         def __str__(self):
#             return f"'{self.title}' by {self.author}"
        
        
# book1=Library.Book("Dune","Herbert")
# print(book1)

# Exercise 2

# 2. Create a School class with a nested Student class. Add a class variable count to Student that increments every time a new student is created. After making 3 students, print Student.count.

class School:
    class Student:
        student_count=0
        def __init__(self, name):
            self.name=name
            School.Student.student_count+=1
            
            
student1=School.Student("Spongebob squarepants")
students2=School.Student("Patrick Star")
students3=School.Student("Sandy Cheeks")
print(School.Student.student_count)
            
        
        
        
    
        
    