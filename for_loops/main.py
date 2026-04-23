# for loops= executes a block of code a fixed number of times.
#            you can iterate over a range, string, sequence, etc.

#A simple programme that counts from 1 to 10
for counter in range(1,11):
    print(counter)
    
#Counting down from 10 to happey new year

for counter in reversed(range(1,11)):
    print(counter)
    
print("HAPPY NEW YEAR")

#iterating over a string

random_name="spongebob squarepants"
for counter in random_name:
    print(counter)
    
# using continue lets you skipp over an interation
#break lets you stop the for loop