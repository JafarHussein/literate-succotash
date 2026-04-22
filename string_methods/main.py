#   String methods in py
name=input("Enter your full Name?: ")
phone_number=input("Please provide your phone number: ")

#Len()->This returns the length of a string
result=len(name)
print(result)

#.find()->This returns the first occurence of a character
first_occurence_of_space=name.find(" ")
print(first_occurence_of_space)

#.rfind()->This returns the last occurence of a character
last_occurence=name.rfind()
print(last_occurence)

#Both the find() and rfind() return indexes

#.capilatize()-Returns a string  capitalized
capitalized_name=name.capitalize()
print(capitalized_name)

#.lower()-Returns a string with all characters in the lowercase
lowercase_name=name.lower()
print(lowercase_name)

#.upper()->Returns a string with all characters in uppercase
uppercase_name=name.upper()
print(uppercase_name)

#isdigit()->Returns a boolean, checks if a string contains only numbers
isdigit_result=name.isdigit()
print(isdigit_result)

#isalpha()->Returns a boolean value, checks if a string only contains alphabetical characters
isalpha_result=name.isalpha()
print(isalpha_result)

#.count(character)->Counts the occurence of a certain character
character_count=phone_number.count("-")
print(character_count)

#.replace("character_being_replaced","character_being_introduced")
new_phone_number=phone_number.replace("-","")
print(new_phone_number)

#string methods available to you
print(help(str))
