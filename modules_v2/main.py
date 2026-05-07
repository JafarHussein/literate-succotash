# Module = a file containing code you want to include in your program. use 'import' to include a module, useful to break up a large program 
# print(help('modules'))
# import math # Now i have access to everything related to the math module
# we can import a module using an alias
# import math as m
#importing something specific from the module
# from math import pi
# print(pi)

# Lets import the module we just created 
import example

main_pi=example.PI
print(main_pi)

radius=35

circle_circumference=example.calculate_circumference(radius)
print(circle_circumference)

circle_area=example.calculate_area(radius)
print(circle_area)
