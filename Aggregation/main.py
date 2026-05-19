# Aggregation = Represents a relationship where one object contains references to one or more independent objects

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def list_books(self):
        return[f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        

library=Library("New York Public Library")
book1=Book("Harry potter and the philosopher stone","J.K.Rolling")
book2=Book("The Hobbit","J.R.R.Tolken")
book3=Book("The color of Magic","Terry pratchet")

#Adding books to the library
library.add_book(book1)

for book in library.list_books():
    print(book)