# Multithreading in py
#threading.thread(target=my_function)
import threading
import time

def walk_dog(name):
    time.sleep(5)
    print(f"You finished walking {name}")
    
def take_trash():
    time.sleep(3)
    print("You have finished taking out the trash")
    
def get_mail():
    time.sleep(1)
    print("You have finished getting the mail")
    
    
walk_dog("scobby")
take_trash()
get_mail()
print("You have finished all the tasks for the day")

#Lets creat a thread to do all the tasks simultaneously

chore1=threading.Thread(target=walk_dog, args=("Scobby",)) # If we have multiple arguements args=(first, second)
chore1.start()


chore2=threading.Thread(target=take_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()


#To ensure the programme executes in a linear manner top to bottom
chore1.join()
chore2.join()
chore3.join()
print("Now this makes the programme wait, before continueing with the rest of the programme")
