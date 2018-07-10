import time
import threading


# helper

# threading.current_thread().name gives the current name 
# of the thread being executed. 

# Blocking program: 
def countdown(count):
    while(count >= 0):
        print("{} Counting down buddy! {}".format(threading.current_thread().name, count))
        count -= 1
        time.sleep(3)

def countup(count):
    while(count <= 10):
        print("{} Counting up buddy! {}".format(threading.current_thread().name, count))
        count += 1
        time.sleep(5)

# Declare threads
t1 = threading.Thread(name="countdown", args=(10,), target=countdown)

# start the thread
t1.start()

t2 = threading.Thread(name="countup", args=(0,), target=countup)
t2.start()

# this will be executed with the main thread
print("All Done!")