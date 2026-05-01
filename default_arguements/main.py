# Default arguements = A default value for certain parameters, default is used when the arguement is omitted, make functions more flexible

def net_price(list_price, discount=0, tax=0.05):
    return list_price * ( 1 - discount) * (1- tax)

print(net_price(500,0,0.05))

import time

def count_timer(start_time, end_time):
    for counter in reversed(range(start_time, end_time+1)):
        print(counter)
        time.sleep(1)
    print("Times up")
    
count_timer(0,45)