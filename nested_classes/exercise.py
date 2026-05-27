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

# class School:
#     class Student:
#         student_count=0
#         def __init__(self, name):
#             self.name=name
#             School.Student.student_count+=1
            
            
# student1=School.Student("Spongebob squarepants")
# students2=School.Student("Patrick Star")
# students3=School.Student("Sandy Cheeks")
# print(School.Student.student_count)


#exercise 3
#  Create a Car class with a nested Engine class. When a Car is created, it should automatically create an Engine instance stored as self.engine. Engine has a start() method returning "Vroom". Print my_car.engine.start().

# class Car:
#     class Engine:
#         def start(self):
#             return "Vroom"
#     def __init__(self, engine):
#         self.engine=Car.Engine()
        
# my_car=Car("Random Engine")
# print(my_car.engine.start())

        
        
    
#Exercise 4
# class Outer:
#     class Inner:
#         val = 10
#     def double(self):
#         return Outer.Inner.val * 2

# o = Outer()
# print(o.double())
# Outer.Inner.val = 7
# print(o.double())

# o is an instance of the class Outter, in the firt initial code inner has a class variable called val which has 10 assigned to it, so the when the double method is called and printed it prints 20, the val is reassigned to 7 and the double value is called and print, the output is 14


#Exercise 5
# 5. Create a Warehouse class with a nested Item class. Add an add_item(name) method to Warehouse that creates and returns an Item. A lot of beginners write return Item(name) inside the method — why does that fail? Fix it.

class Warehouse:
    warehouse_items=[]
    class Item:
        def __init__(self, name):
            self.name=name
    def add_items(self, name):
        new_item=Warehouse.Item(name)
        Warehouse.warehouse_items.append(new_item)
        return [ item.name for item in Warehouse.warehouse_items]
    
    
warehouse=Warehouse()
item_list=warehouse.add_items("Toothbrush")
print(item_list)
    
    