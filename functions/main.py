# Functions- some instructions packaged togerther to perform some baction

#Sample random function
def say_hello():
    for counter in range(0,4):
        print("Hello friend")

#Giving a parameter to a function
def custom_greeting(greeting, name='You'):
    print(f"{greeting},{name}")
    
#Positional arguements are assigned based on their order  in the function call,requiring strict alignment with the parameter definition

#Keyword arguements use name=value pairs, making the order irrelevant, improving code readability and allowing for optional parameters

#Positional arguements
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")
    
describe_pet('dog','Buddy')

#Keyword arguements
describe_pet(name="Buddy", animal="dog")

courses=['Mathematics','Art']
info={'name':'John', 'age':22}

def student_info(*args,**kwargs):
    print(*args)
    print(**kwargs)
    
student_info(*courses, **info)

#Default arguements= A default value for certain parameters default is used when that arguement is ommited make your functions more flexible, reduces # of arguements

def net_price(list_price, discount=0, sales_tax=0.05):
    return list_price * (1 - discount) * (1 + sales_tax)

print(net_price(500))

#Key word arguments= an arguement preceded by an identifier helps with readability.Order of arguements doesn't matter

def say_hello_3(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")
    
say_hello_3("Hello","Mr.","Spongebob","Squarepants")
say_hello_3(greeting="Hello",title="Mr.",first_name='Spongebob', last_name="SquarePants")
#With keyword arguments the order of arguments doesn't really matter

