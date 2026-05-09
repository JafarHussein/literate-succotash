# Object= A bundle of related attributes and methods

#class used to design the structure of an object

from car import Car       
car1= Car("Mustang",2024,"red",True)

print(car1.Model)
print(car1.year)
print(car1.color)
if car1.for_sale == True:
    print("The car is for sale")
else:
    print("The car is not for sale")
    

car2=Car("Corvette",2026,"Blue",False)

print(car2.Model)
print(car2.year)
print(car2.color)
if car1.for_sale == True:
    print("The car is for sale")
else:
    print("The car is not for sale")
    
car3=Car("Charger", 2011,"Green",False)

print(car3.Model)
print(car3.year)
print(car3.color)
if car1.for_sale == True:
    print("The car is for sale")
else:
    print("The car is not for sale")
    
         
         