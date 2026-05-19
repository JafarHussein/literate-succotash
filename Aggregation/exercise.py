#Exercise 1 — Basic Containment
#Create a Battery class with a capacity attribute. Then create a Phone class that contains a Battery object. #Print the phone's battery capacity through the phone.

# Build two classes, Battery and Phone, where Battery has an __init__ method that takes capacity and a charge() method that prints "Charging...", and Phone has an __init__ method that takes make, model, and a battery object as attributes. Then implement it by creating a Battery object with capacity 4000, passing it into a Phone object with make "Samsung" and model "S24", printing the phone's make, model, and battery capacity, and finally calling charge() through the phone object — not directly on the battery.

class Battery:
    
    def __init__(self,capacity):
        self.capacity=capacity
        
    def charge(self):
        print("Charging....")
        
class Phone:
    
    def __init__(self, make,model,battery):
        self.make=make
        self.model=model
        self.battery=battery
        

my_battery=Battery(4000)

my_phone=Phone("Samsung","S24",my_battery)

print(my_phone.make)
print(my_phone.model)
print(my_phone.battery.capacity)

my_phone.battery.charge()