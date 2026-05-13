# Duck typing
# 'If it looks like a duck and quacks like a duck, it must be a duck'

class Animal:
    is_alive=True
    
class Dog(Animal):
    def speak(self):
        print("WOOF")
        
class Cat(Animal):
    def speak(self):
        print("meow")
        
animals=[Dog(),Cat()]

for animal in animals:
    animal.speak()