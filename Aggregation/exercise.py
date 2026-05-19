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

# Create a Student class with name and grade as attributes, and a Classroom class that holds a list of Student objects as an attribute. Then create at least 3 student objects, pass them into a Classroom object, and add a method to Classroom that prints all the student names.

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        
class ClassRoom:
    def __init__(self,name):
        self.name=name
        self.list_students=[]
        
    def add_student(self,student):
        self.list_students.append(student)
        
    def print_students(self):
        for student in self.list_students:
            print(student.name, student.grade)
            
    def top_student(self):
        top= self.list_students[0]
        
        for student in self.list_students:
            if student.grade > top.grade:
                top=student
                
        return top
            
    
classroom=ClassRoom("classroom-1")
        
        
student1=Student("Spongebob Squarepants", 75)
student2=Student("Patrick Star",80)
student3=Student("Sandy cheeks", 96)

classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)

classroom.print_students()


# Create an Employee class with name and salary as attributes, and a Department class that holds a list of Employee objects. Add an add_employee() method to Department, a total_salary() method that returns the total salary bill of all employees, and a highest_paid() method that returns the employee with the highest salary. Then create at least 3 employees, add them to a department, and print the total salary bill and the highest paid employee's name and salary.


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def __str__(self):
        return f"{self.name} earns {self.salary}"
        
class Department:
    
    def __init__(self,name):
        self.name=name
        self.employee_list=[]
        
    def add_employee(self,employee):
        self.employee_list.append(employee)
        
    def highest_paid(self):
        
        highest_paid_employee=self.employee_list[0]
        
        for employee in self.employee_list:
            if employee.salary > highest_paid_employee.salary:
                highest_paid_employee=employee
        return highest_paid_employee
    
    def total_salary(self):
        total_employee_salary=0
        
        for employee in self.employee_list:
            total_employee_salary+=employee.salary
            
        return total_employee_salary
    
department1=Department("Krusty Krab")
    
employee1=Employee("SpongeBob",3000)
employee2=Employee("Patrick",4000)
employee3=Employee("Sandy",5000)

#Adding employees to the department

department1.add_employee(employee1)
department1.add_employee(employee2)
department1.add_employee(employee3)
print(department1.highest_paid())
print(department1.total_salary())

        


