# Decorator = A function that extends the behavior another function w/o modifying the base function

# @addsprinkles
# get_ice_cream("vanilla")


# A function that takes another function as input and returns a new enhanced function without modifying the original code


def add_sprinkles(func):
    
    def wrapper():
        print("Adding sprinkles")
        func()
    return wrapper


@add_sprinkles
def get_ice_creame(flavour):
    print(f"Here is your {flavour} ice cream")