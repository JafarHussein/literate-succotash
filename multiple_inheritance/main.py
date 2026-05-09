# multiple inheritance = inherit from more than one parent c(A,B)
class Animal:
    def __init__(self, name):
        self.name=name
    def eat(self):
        print("All animals eat")
    def sleep(self):
        print("This animal is sleeping")
        
class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")
        
class Predator(Animal):
    def hunt(self):
        print("This is animal is hunting")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

#multilevel inheritance= inherit from a another parent A - B(A) - C(B)

        
# Prey and predator will inherit from the animal class

