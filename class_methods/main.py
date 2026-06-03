# class methods = Allow operations related to the class itself , it takes (cls) as the first parameter which represents the class itself

class Student:
    count=0
    total_gpa=0
    def __init__(self, name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa
    #This is an instance method  
    def get_info(self):
        return f"{self.name}, gpa={self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students = {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        average_gpa=0.00
        
        if cls.count == 0:
            return 0.00
        else:
            average_gpa=cls.total_gpa/cls.count
            return f"The average gpa is {average_gpa:.2f}"
        
    
    
print(Student.get_count())
student_1=Student("Spongebob Squarepants", 2.5)
student_2=Student("Patrick", 1.5)
student_3=Student("Sandy", 4.0)
print(Student.get_count())
print(Student.get_average_gpa())
        