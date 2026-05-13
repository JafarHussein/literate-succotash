# super(): A function used in a child class to call methods from a parent class, allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, is_filled, color):
        self.is_filled=is_filled
        self.color=color
        
class Circle(Shape):
    
    PI=3.1415
    
    def __init__(self,is_filled, color, radius):
       super().__init__(is_filled,color)
       self.radius=radius
       
    def calculate_circumfrence(self):
        circumfrence= 2 * Circle.PI * self.radius
        return f" Your circumfrence is {circumfrence:.2}cm"
    
    def calculate_area(self):
        area=Circle.PI * self.radius * self.radius
        return f"The area of the circle is {area:,2f}square centimeters"
        

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
       
circle=Circle(True, 'red',10)
square=Square(False,'blue',20)
rectangle=Rectangle(True, 'green',5,15)

circle.calculate_circumfrence()
circle.calculate_area()

square.calculate_perimeter()
square.calculate_area()

rectangle.calculate_perimeter()
rectangle.calculate_area()
       
       
    
