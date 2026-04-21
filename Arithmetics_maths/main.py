import math

# Sample programme to determine if a number is even or odd
random_number=int(input("Please provide any random whole number of your choosing: "))
if random_number % 2 == 0:
    print(f"{random_number} is an even number")
else:
    print(f"{random_number} is an odd number")
    
#A simple programme to calculate the circumfrence and area of a circle

random_radius=float(input("Please provide the radius of the circle: "))
PI=math.pi
circumfrence=PI * 2 * random_radius
print(f"The circumfrence of your circle is {circumfrence} centimeters")

#Calculating the area of the circle
area=PI * pow(random_radius, 2)
print(f"The area of your circle is {area} square centimeters")