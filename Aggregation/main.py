#Aggregation is a way to combine objects in python where one class contains another class , but they can both exist independently

class Library:
    def __init__(self, name):
        self.name=name

class Book:
    def __init__(self, title,author):
        self.title=title
        self.author=author
        
library=Library("New York public library")

book1=Book("Atomic Habits","J.K.Rowling")
book2=Book("The Hobbit","J.")