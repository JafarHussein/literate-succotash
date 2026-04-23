# Lists are a built in, ordered and mutable collection used to store multiple items  in a single variable
# Mutable means you can add or remove items after the list has already been created

courses=['History','Mathematics','Comp sci','Physics']
#You can access the items in the list using indexing , for list the indexes start at 0
print(courses[0]) # This is going to print the first item in the list

#You can also use negative indexing
print(courses[-1]) #This is going to print the last item in the list regardless of the length

#You can also print a range of values
for counter in range(0, len(courses)):
    print(courses[counter])
    
#list methods available to us
#1. append(value)->This adds an item at the end of the list
courses.append('Art')
print(courses)

#2. .insert(index, value)->This inserts a value at a specific index
courses.insert(0,'Engineering')
print(courses)

#3. .extend()->This method is used to combine 2 lists in one joint list
courses_2=['Medicine','Hospitality']
courses.extend(courses_2)
print(courses)

#4. .remove('value')->This methods is used to remove items
courses.remove('Hospitality')
print(courses)

#5. .pop()->This method removes the last item from the list by default, it returns the value that was removed
courses.pop()
print(courses)

#6. reverse()->This reverses the list in place
courses.reverse()
print(courses)

#7. .sort()->This sorts the list in alphabetical order
courses.sort()
print(courses)

nums=[2,8,9,10,11,14,25]
nums.sort()
print()
# Numbers are sorted in ascending order

# If you pass an argument of reverse=True, this sorts in reverse in order

# .sorted(value)->This returns a sorted version of a list
sorted_list=sorted(courses)
print(sorted_list)


# min(list)->This returns the minimum value in a list
#max(list)-> This returns the maximum value in a list
#sum(list)->This returns the sum of all the list items

# .index('value)->If you want to locate the index of a particular value in a list , you use .index( ) method, this returns a valueError if you such for an item that doesn't exist
index_comp_sci=courses.index('Comp Sci')
print(index_comp_sci)


#If you want to know if an item is in the list and get a true or false asnwer you use the 'in' operator

print('Comp Sci' in courses)

# Turning a list into a string with comma seperated values
courses_str=', '.join(courses)
print(courses_str)

#Turning a string into a list
new_list=courses_str.split(", ")
print(new_list)

