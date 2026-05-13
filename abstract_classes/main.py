# Abstract classes: A class that cannot be instantiated on its own; meant to be sub classes
#abstract base classes, Abstract base class
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def __init__(self, model, year, color):
        self.model=model
        self.year=year
        self.color=color
    def go(self):
        print(f"You drive {self.model}")
    def stop(self):
        print(f"You stopped the {self.model}")
        

car1= Car("Mustang",2024,"Red")
print(car1.model)
print(car1.year)
print(car1.color)
car1.go()
car1.stop()

