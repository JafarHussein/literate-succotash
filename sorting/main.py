# Sorting in py .sort() or sorted()
#lists[], tuples(), Dictionaries{"":""}, objects


#lets sort a list 
fruits=["Oranges","Banana","Apples", "Coconuts"]
fruits.sort()
print(fruits)

#Sorting the fruits in reverse order
fruits.sort(reverse=True)
print(fruits)

#Lets try this with numbers
random_numbers=[1,2,3,4,5,6,7,8,9,10]
random_numbers.sort(reverse=True)
print(random_numbers)

#Lets move on to Tuples
fruits_tupel=("Banana","Oranges", "Apples","Coconut")
print(sorted(fruits_tupel))

#Now that if you use the sorted method on a tupel it returns a list

#Lets try sorting numbers in reverse

numbers_tupel=(1,2,3,4,5,6,7,8,9,10)
print(sorted(numbers_tupel, reverse=True))


#Now Dictionaries, lets try sorting in Dictionaries


serving_info={"Banana":310,
              "Oranges":250,
              "Apples":120,
              "Coconuts":110}

serving_info=dict(sorted(serving_info.items()))
print(serving_info)





