import time
import threading


# Blocking program: 
def countdown(count):
    while(count >= 0):
        print("Counting down buddy! {}".format(count))
        count -= 1
        time.sleep(3)


# Declare threads
# format of the thread name of the thread (can be anything), pass in the argurment, 
# and then finally the target function that needs to be run on the thread
t1 = threading.Thread(name="countdown", args=(10,), target=countdown)

# start the thread
t1.start()

# this will be executed with the main thread
print("All Done!")