# Polymorphism : Greek word that means to have many faces 

#Polymorphism through inheritance

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def calculate_area(self):
        pass
    

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius=radius
    
    def calculate_area(self):
        return 3.1415 * self.radius

class Square(Shape):
    
    def __init__(self, side):
        self.side=side
    
    def calculate_area(self):
       return self.side * self.side
   

class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base=base
        self.height=height
    
    def calculate_area(self):
       return 0.5 * self.base * self.height

shapes=[Circle(10.5),Square(3.6),Triangle(10,15)]

for shape in shapes:
    print(f"{shape.calculate_area():.2f} square centimeters")