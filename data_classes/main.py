# Data class = A special kimd of class that's designed mostly for holding data without writing a lot of the boilerplate code for regular classes

#Here is a normal class
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.alive=True
        
    def __repr__(self):
        return f" Name:{self.name}, age={self.age} isAlive:{self.isalive}"
    

person1=Person("SpongeBob", 27)
person2=Person("Patrick", 35)



#Using dataclass

from dataclasses import dataclass, field

@dataclass (frozen=True) #This make the objects from this class immutable
class People:
    name:str
    age:int
    #The helper function helps field helps make the password hidden
    password:str = field(repr = False)
    is_alive:bool=True
    
    def __post__init__(self):
        if self.age<=0:
            raise ValueError("Age needs to be a positive number greater than 0")
    
    
people1=People("Sandy", 35)
print(people1.name)
print(people1.age)
print(people1.is_alive)

#For data classes you don't need to explicitly write the dunder methods
        