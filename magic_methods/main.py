# Magic methods= Dunder methods, __init__, __str__, __eql__ they are automatically by many of python's inbuilt operations.They allow developers to customize the behavior of objects


class Book:
    def __init__(self, title, author, number_of_pages):
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
        
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __getItem__(self, key):
        
        if key == 'Title':
            return self.title
        
        elif key == 'Author':
            return self.author
        
        elif key == 'Num_pages':
            return self.number_of_pages
        
        else:
            return "Internal Error"
    
    
    
book1=Book("The Hobbit","J.R.R. Tolkien", 310)
book2=Book("Harry Potter and the Philosopher stone","J.K.Rowling",223)
book3=Book("The lion, witch and the wardrobe","C.S.Lewis", 172)

print(book1)
print(book2)
print(book3)
print(book1==book2)

