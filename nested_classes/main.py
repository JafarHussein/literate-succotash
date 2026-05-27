# Nested class

class Company:
    class Employee:
        
        def __init__(self, name,position):
            self.name=name
            self.position=position
        
        def get_details(self):
            return f"{self.name}, {self.position}"
    
    def __init__(self, name):
        self.name=name
        self.employees=[]
        
    def add_employees(self, name,position):
        new_employee=self.Employee(name, position)
        self.employees.append(new_employee)
        
    def list_employees(self):
        return [employee.get_details()for employee in self.employees]
    
    
company=Company("Krusty Krab")
company.add_employees("Eugene Krabs","Manager")
company.add_employees("Squirdward", "Cashier")

#Printing employees in the company

for employee in company.list_employees():
    print(employee)