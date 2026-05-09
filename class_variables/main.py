# class Variable - a variable that belongs to the class itself rather than instance of that class, this variables are defined outside the constructor

from student import Student

student1=Student("Spongebob", 27)
student2=Student("Sandy",25)
student3=Student("Squirdward",55)
student4=Student("Patrick", 25)

print(student1.name)
print(student1.age)
print(student1.class_year)
#Its good practise to access class in this way
print(Student.class_year)

print(student2.name)
print(student2.age)
print(student2.class_year)
#Good practise
print(Student.class_year)

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")