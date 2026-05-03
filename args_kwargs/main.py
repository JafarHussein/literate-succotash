# *args= allows you to pass multiple non key arguements, tupel
# **kwargs= allows you to pass multiple keyword arguements, dictionary

def add(a,b):
    return a + b

print(add(1,2))

# Modifying the function to accept multiple arguements instead of 2 only

def add_1(*args):
    sum=0
    for arg in args:
        sum+=arg
    return sum

print(add_1(1,2,3,4))

#**kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123 fake strt", city="detroit", state="Michigan",zip="00102001")
        
