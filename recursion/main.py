# Recursion= a function that calls itself from within helps visualize a complex problem into basic steps


#Iterative 
# def walk(steps):
#     for counter in range(0, steps+1):
#         print(f"You take step number : {counter}")
        
# walk(100)


#Recursion

def walk(steps):
    if steps == 0:
        return
    walk(steps-1)
    print(f"You take step #{steps}")
    
walk(100)