# Now we import the module we just created 
import my_module
import sys
import random

#Instead typing the whole module we can just do:
#import my_module as mm
available_courses=['Mathematics','History','Physics']

#using the function from the module we just created
mathematics_index=my_module.find_index(available_courses, 'Mathematics')
print(mathematics_index)

#We can import the only thing we need from a module using this:
from my_module import test
print(test)
#The disadvantage of this is you only get the thing you have imported not the whole thing

print(sys.path)

#Assuming that the module you want to import is not in the same directory as the script you are running, you can add it manually
# import sys
# sys.path.append(Actual_path)
