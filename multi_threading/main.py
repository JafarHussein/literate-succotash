# Multi threading= used to perform multiple tasks concurrently, good for i/o bound tasks like reading files or fetching data from an api

#We need this module in order to perform multithreading
import threading
import time

def walk_dog():
    time.sleep(8)
    print("We are walking the dog")
    
def take_trash():
    time.sleep(23)
    print("You are taking out the trash")
    
def get_mail():
    time.sleep(4)
    print("You are getting the mail")
    
    
chore1=threading.Thread(target=walk_dog)
#start this thread
chore1.start()


chore2=threading.Thread(target=take_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()

# Wanting a program to wait

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")

#Assuming one of the functions takes an arguement
chore1=threading.Thread(target=walk_dog, args=("Scooby",))