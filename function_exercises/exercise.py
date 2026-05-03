# Create a simple function that takes a name and an age and returns a personlaized greeting

def greet_func(name, age):
    if age>0 and age<=10:
        print(f"Heey {name}, whatsapp buddy")
    elif age>10 and age<=15:
        print(f"Wagwan {name}")
    else:
        print(f"Hello {name}, how is your day going so far ?")
    
greet_func("SpongeBob", 17)

# 2. Write a function that takes in the parameter of a shape and calculates the area based on the shape

import math

def calculate_area(shape):
    user_shape=shape.lower()
    if user_shape == 'circle':
        circle_radius=float(input("Provide the radius of the circle: "))
        PI=3.1415
        area= PI * math.pow(circle_radius,2)
        print(f"The area of the circle is {area:.2f}")
    elif user_shape == 'rectangle':
        rectangle_length=float(input("Please provide the length of the rectangle: "))
        rectangle_width=float(input("Please provide the width of the rectangle: "))
        rectangle_area=rectangle_length * rectangle_width
        print(f"The area of the rectangle is {rectangle_area:.2f}")
    else:
        print("Error: we can only calculate the area of either a circle or a rectangle")
        
calculate_area("square")
calculate_area("rectangle")
calculate_area("circle")

# 3. currency conveter 

def currency_conveter():
    amount=0
    currency=None
    print("This is a simple currency conveter programme")
    amount_usd=float(input("How much many in usd do you have: "))
    while amount_usd<=0:
        amount_usd=float(input("Please provide the amount you have in usd: "))
    currency=input("To which currency do you intend to convert the usd to: ")
    rate=float(input("Please provide the convertion rate: "))
    amount=amount_usd * rate
    print(f"Your money has been converted from usd to {currency}")
    print(f"The total amount is {amount:.2f}")

currency_conveter()

# A simple function that checks if a password is valid
import string
def password_checker(password):
    lower_chars='abcdefghijklmnopqrstuvwxyz'
    upper_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number_chars='1234567890'
    symbol_chars=string.punctuation
    has_lower=False
    has_upper=False
    has_digits=False
    has_symbols=False
    for char in password:
        if char in lower_chars:
            has_Lower=True
    for char in password:
        if char in upper_chars:
            has_upper=True
    for char in password:
        if char in number_chars:
            has_upper=True       
    for char in password:
        if char in symbol_chars:
            has_symbols=True
    
    if len(password)>=8:
        if has_lower and has_upper and has_digits and has_symbols:
            print("Your password is good to go")
        else:
            print(f"your password is {len(password)} characters long but its weak")
    else:
        print("Your password doesn't meet the minimum requirements")
        
password_checker("password")

#A simple py function that converts the temperature from celcius to farenheit and vice versa

def temperature_conveter():
    final_temp=0
    temp_value=float(input("Please provide your temperature value: "))
    initial_unit=input("whats the current unit of the temperature value(celcius/Fahrenheit): ").lower()
    final_unit=input("whats going to be the final unit of the temperature value(celcius/Fahrenheit): ").lower()
    if initial_unit == 'celcius' and final_unit == 'fahrenheit':
        final_temp=(temp_value * 1.8) + 32
        print(f"You have converted the temperature from {initial_unit} to {final_unit}, so the temperature is {final_temp} {final_unit}.capitalize()")
    elif initial_unit == 'fahrenheit' and final_unit == 'celcius':
        final_temp=((temp_value-32)/1.8)
        print(f"You have converted the temperature from {initial_unit} to {final_unit}, so the temperature is {final_temp} {final_unit}.capitalize()")
    else:
        print("ERROR")
        
temperature_conveter()
    
    