# An exercise to test my understanding on the concept of nested classes

#exercise 1
# 1. Create a Library class with a nested Book class. Book takes a title and author. Its __str__ should return "Dune by Herbert". Instantiate a book using Library.Book(...) and print it.
class Library:
    class Book:
        def __init__(self, title, author):
            self.title=title
            self.author=author
            
        def __str__(self):
            return f"'{self.title}' by {self.author}"
        
        
book1=Library.Book("Dune","Herbert")
print(book1)
        
        
        
    
        
    