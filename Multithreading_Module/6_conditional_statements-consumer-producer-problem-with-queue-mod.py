import threading

import time 
import random

import queue

_queue = queue.Queue(10)


# class should be inherited from the threading.Thread 
class ProducerThread(threading.Thread):
    # when inheriting from the 
    # thread  make sure to override the run function. 
    def run(self):
        numbers = range(5)
        # globalizing the variable. 
        global _queue

        while True:
            number = random.choice(numbers)
            _queue.put(number)
            print("Produced {}".format(number))
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def run(self):
        global queue

        while True:
            number = _queue.get()
            _queue.task_done()
            print("Consumder {}".format(number))
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