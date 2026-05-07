# match-case-statement= An alternative to using many elif statements, executes some code if a value matches a case

def return_day(day):
    match day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("saturday")
        case _:
            print("Error")
            
return_day(3)
        