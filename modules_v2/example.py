import math as m

PI=3.14159

def square(num):
    return m.pow(num,2)

def cube(num):
    return m.pow(num,3)

def quad(num):
    return m.pow(num,4)

def calculate_circumference(radius):
    return 2 * PI * radius

def calculate_area(radius):
    return PI * m.pow(radius,2)
