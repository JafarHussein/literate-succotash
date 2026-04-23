# Format specifiers = {:flags} format a value based on what flags are insereted
# .(number)f->Round to that many decimal places(fixed point)
price1=3.14519
price2=-987.65
price3=12.34

#Rounding off to 2 decimal places
print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")

#Allocating some spaces before displaying anything
print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

#Zero padding the spaces
print(f"Price 1 is {price1:010} ")
print(f"Price 2 is {price2:010} ")
print(f"Price 3 is {price3:010} ")

#left justify a value when displaying
print(f"price 1 is {price1:<}")

#Right justify
print(f"Price 1 is {price1:>}")

#Center align 
print(f"price 1 is {price1:^}")

#preceding a number with the appropriate symbol
print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

#Ensuring all the outputs are aligned 
print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")

#The thousand seperators using a commar
print(f"Price 1 is {price1:,}")




