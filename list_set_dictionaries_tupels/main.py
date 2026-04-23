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

# The "Library Inventory" Challenge
# Setup:
# Start with this list of books:
# books = ['Physics', 'Mathematics', 'History', 'Comp Sci']
# The Task:
# Write a script that performs these specific steps in order:
# Additions: Add 'Bio' to the end of the list and 'Art' to the very beginning.
#Adding art to the very beginning
books=['Physics','Mathematics','History','Compsci']
books.insert(0,'Art')
books.append('Bio')
print(books)
# The Merger: You found a box of extra books: extra_books = ['Chemistry', 'French']. Add these to your books list so it stays as one single list.
extra_books=['Chemistry','French']
books.extend(extra_books)
print(extra_books)
# The Audit:
# Find and print the index of 'Mathematics'.
mathematics_index=books.index('Mathematics')
print(mathematics_index)
# Check if 'Geography' is in the list and print the True/False result.
if 'Geography' in books:
    print("There is a Geography book in the library")
else:
    print("There is no Geography book in the library")
# Cleaning: Remove 'French' from the list using its name. Then, use .pop() to remove the very last book and print the name of the book you just removed.
books.remove('French')
last_book_removed=books.pop()
print(last_book_removed)
# Organization: Sort the list in alphabetical order, then reverse that order.
sorted_books=sorted(books)
print(sorted_books)

books.sort(reverse=True)
print(books)
# The Report:
# Turn the final list into a single string where each book is separated by a slash (/).
books_str='/'.join(sorted_books)
print(books_str)
# Split that string back into a new list called final_list and print it.
final_list=books_str.split("/")
# Bonus (Numbers): Create a list called prices = [20, 50, 15, 40]. Print the total cost (sum) and the cheapest (min) price.
prices = [20, 50, 15, 40]

max_price=max(prices)
print(max_price)

minimum_price=min(prices)
print(minimum_price)

total_sum=sum(prices)
print(total_sum)

#Tuples
# Tuples are very similar to list the one major difference is that tupels are not mutable

courses_tuples=('History','Mathematics','Physics','Compsci')
print(courses_tuples)

