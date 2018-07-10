import threading

# initialize the buffer and the locking mechanism. 
# we are going to call the Lock directly from the threading library. 
counter_buffer = 0
counter_lock = threading.Lock()

# buffer will iterate between the number 0 - 100 
COUNTER_MAX = 1000000

def counsumer1_counter():
    # calling the counter variable as global
    global counter_buffer
    # iterate till we reach the max defined in the buffer. 
    for i in range(COUNTER_MAX):
        # acuires the lock 
        counter_lock.acquire()
        # increment the buffer
        counter_buffer += 1
        # release the counter 
        counter_lock.release()

def counsumer2_counter():
    # calling the counter variable as global
    global counter_buffer
    # iterate till we reach the max defined in the buffer. 
    for i in range(COUNTER_MAX):
        # acuires the lock 
        counter_lock.acquire()
        # increment the buffer
        counter_buffer += 1
        # release the counter 
        counter_lock.release()

t1 = threading.Thread(target=counsumer1_counter)
t2 = threading.Thread(target=counsumer2_counter)

t1.start()
t2.start()

# in order to make sure that the main thread doesnt get run and complete before the 
# t1 and t2 thread call the below. Which will make t1 and t2 join the main thread. 
t1.join()
t2.join()

print(counter_buffer)