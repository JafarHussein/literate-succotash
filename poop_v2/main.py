# Why do we use classes: a blueprint that bundles data and the functions that use that data into a single entity, they are essential for managing complexity as programms grow

class Employee:
    raise_amount=1.04
    def __init__(self, name,pay, email_address, actions):
       self.name=name
       self.pay=pay
       self.email_address=email_address
       self.actions=actions
    def display_data(self):
        print(f"Name {self.name}")
        print(f"Pay: ${self.pay}")
        print(f"email address: {self.email_address}")
        print("Here are the actions that the employee is able to perform in the organization")
        for action in self.actions:
            print(action)
            print()
    def calculate_bonus(self, hours, hpay):
        bonus=hours * hpay
        print(f"You worked {hours} extra hours for a pay of {hpay}/hr, your bonus is ${bonus}")
    def calculate_raise(self):
       salary_raise=self.pay + (self.pay * Employee.raise_amount)
       return f"${salary_raise:.2f}"
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,employee_str):
        name,pay,email,actions=employee_str.split('-')
        return cls(name,pay,email,actions)
    
       
        
        
        
    
#Instance variables, unique data for a specific instance

employee_1=Employee("Spongebob SquarePants",1200,"123fake@gmail.com",["Cooking","Jely fishing","Bubble blowing"])

employee_2=Employee("Patrick Start",0,"patrickstar@gmail.com",['Ice cream eating','Jelly fishing'])

employee_3=Employee("Squirdward Tentacles",3500,"crunkysquidwardtenticles@gmail.com",['Music', 'Painting'])

employee_1.display_data()
employee_1.calculate_bonus(3,1.2)

employee_2.display_data()
employee_2.calculate_bonus(1,0.05)

# When you call a method on a class you need to provide the instance
Employee.display_data(employee_3)
Employee.calculate_bonus(employee_3,2,20)

print(employee_1.calculate_raise())

# Class variables : Variables that are shared among all the instances of a class

#class methods and static methods
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)


