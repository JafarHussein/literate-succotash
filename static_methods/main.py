# Static methods= A method that belongs to a class rather than an object , usuallyt used for general utility functions

class Employee:
    def __init__(self, name,position):
        self.name=name
        self.position=position
        
    def get_info(self):
        return f"{self.name}, {self.position}"
    
    #Lets create a static method
    
    @staticmethod
    def is_valid_position(position):
        valid_positions=['Fry cook',"Manager","Cashier","Janitor"]
        return position in valid_positions
    
    
print(Employee.is_valid_position("Teacher"))
print(Employee.is_valid_position("Janitor"))
employee_1=Employee("Eugene","Manager")
employee_2=Employee("Spongebob","Fry cook")
employee_3=Employee("Squirdward","Cashier")
print(employee_1.get_info())
print(employee_2.get_info())

