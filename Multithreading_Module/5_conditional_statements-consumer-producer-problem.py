import threading

import time 
import random

queue = []

MAX_ITEMS = 10

# A factory function that returns a new condition variable object. 
# A condition variable allows one or more threads to wait until
# they are notified by another thread. 
condition = threading.Condition()

# class should be inherited from the threading.Thread 
class ProducerThread(threading.Thread):
    # when inheriting from the 
    # thread  make sure to override the run function. 
    def run(self):
        numbers = range(5)
        # globalizing the variable. 
        global queue

        while True:
            # the below method tries to hold the lock on the thread. 
            condition.acquire()
            if len(queue) == MAX_ITEMS:
                print("Queue is full, producer is waiting")
                # the below methods waits for the buffer to be available. 
                condition.wait()
                print("Space in queue, Consumer notified producer")
            number = random.choice(numbers)
            queue.append(number)
            print("Produced {}".format(number))
            # sends a signal to intiamate any threads that is in waiting state. 
            condition.notify()
            # releases the lock held by the acuqire method. 
            condition.release()
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def run(self):
        global queue

        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait()
                print("Producer added something to queue and notify the Consumer")
            number = queue.pop(0)
            print("Consumder {}".format(number))
            condition.notify()
            condition.release()
            time.sleep(random.random())

producer = ProducerThread()
# non daemon threads will execute for ever and will not terminate 
# Hence daemonizing the threads. 
producer.daemon = True
producer.start()

consumer = ConsumerThread()
# non daemon threads will execute for ever and will not terminate 
# Hence daemonizing the threads. 
consumer.daemon = True
consumer.start()

# Keeping the main thread alive so that when we interrupt the main thread
# the daemon thread also gets killed. 
while True:
    time.sleep(1)