capitals={'USA':'Washington D.C',
          "KENYA":"Nairobi",
          "TANZANIA":'Dodoma',
          "RUSSIA":'Moscow'}

# Getting one of the values

usa_capital=capitals.get("USA")
print(usa_capital)
#.get(key)-This method returns the value associated with a particular key, if the key is non existent it returns none

if capitals.get("GERMANY")== None:
    print("Germany is not located in the capitals dictionary")
else:
    print("That capital is located in the capitals dictionary")
    
#Updating a dictonary
capitals.update({'GERMANY':'Berlin'})
print(capitals)

#Removing a key from the dictionary
capitals.pop('RUSSIA')
print(capitals)

#.popitem()->This removes the last key, value pair in the dictionary
#.clear()->This removes everything from the dictionary
#.keys()->This returns all the keys without the values
for keys in capitals.keys():
    print(keys)
#.values()->This returns all the values without the key
for value in capitals.values():
    print(value)
    
for key, value in capitals.items():
    print(f"{key}->{value}")