# Exception = An event that interupts the normal flow of a programme(division by zero, typeError, valueError)
#1.try 2.Except 3.Finally


try:
    first_number=int(input("Choose any random number greater than 0: "))
    second_number=int(input("Choose a divisor: "))
    results=float(first_number/second_number)
except ZeroDivisionError:
    print("You can't Divide by zero, ediot")
except ValueError:
    print("Only numbers are accepted")
#The finally block executes always
finally:
    print("The code ran succefully my friend")    
    