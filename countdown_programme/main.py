import time

user_time=int(input("Please enter the count down time in seconds: "))
for counter in reversed(range(0, user_time+1)):
    print(counter)
    time.sleep(1)
    
print("Times up")