#Composition= The composed object directly owns its components, which cannot exist independently

class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power
        

class Wheel:
    def __init__(self,size):
        self.size=size
        

class Car:
    def __init__(self, make,model,horse_power,wheel_size):
        self.make=make
        self.model=model
        self.engine=Engine(horse_power)
        self.wheels=[Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.model} {self.make} {self.engine.horse_power}(hp)"      
        
        
car1=Car("ford","mustang",500,18)
print(car1.display_car())

