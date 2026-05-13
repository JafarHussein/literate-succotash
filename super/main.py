# super(): A function used in a child class to call methods from a parent class, allows you to extend the functionality of the inherited methods

class Shape:
    
    def __init__(self, is_filled, color):
        self.is_filled=is_filled
        self.color=color
        
    def describe_shape(self):
        print(f"its {self.color}")
        print("it is filled" if self.is_filled else "not filled")
        
        
class Circle(Shape):
    
    PI=3.1415
    
    def __init__(self,is_filled, color, radius):
       super().__init__(is_filled,color)
       self.radius=radius
       
    def calculate_circumfrence(self):
        circumfrence= 2 * Circle.PI * self.radius
        return f" Your circumfrence is {circumfrence:.2f}cm"
    
    def calculate_area(self):
        area=Circle.PI * self.radius * self.radius
        return f"The area of the circle is {area:.2f}square centimeters"
    
    def describe(self):
        print("This is a circle")
        #This is extending the functionality of the super class method
        super().describe_shape()
        

class Square(Shape):
    
    def __init__(self,is_filled,color, side):
        super().__init__(is_filled,color)
        self.side=side
    
    def calculate_perimeter(self):
        perimeter= 4 * self.side
        return f"The perimeter of the square is {perimeter:.2f}cm"
    
    def calculate_area(self):
        area= self.side * self.side
        return f"The area of the square is {area:.2f} square centimeters"
    
    def describe(self):
        print(f"This is a sqaure with an area of {self.side * self.side} square centimeters")
        super().describe_shape()
    
class Rectangle(Shape):
    
    def __init__(self,is_filled,color, width, height):
       super().__init__(is_filled,color)
       self.width=width
       self.height=height
       
    def calculate_perimeter(self):
        perimeter= 2 * (self.width + self.height)
        return f"The perimeter of the rectangle is {perimeter:.2f}cm"
    
    def calculate_area(self):
        area= self.width * self.height
        return f"The area of the rectangle is {area:.2f} square centimeters"
    
    def describe(self):
        print(f"This is a rectangle with an area of {self.width * self.height} square centimeters")
        super().describe_shape()
       
circle=Circle(True, 'red',10.0)
square=Square(False,'blue',20.0)
rectangle=Rectangle(True, 'green',5.0,15.0)

print(circle.calculate_circumfrence())
print(circle.calculate_area())

print(square.calculate_perimeter())
print(square.calculate_area())

print(rectangle.calculate_perimeter())
print(rectangle.calculate_area())

circle.describe()
square.describe()
rectangle.describe()
       
       
    
