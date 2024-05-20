from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire() 
                                        #Critical section
            if len(queue) == MAX_NUM:
                print ("Queue full, producer is waiting")
                condition.wait()
                print ("Space in queue, Consumer notified the producer")
            num = random.choice(nums)
            queue.append(num)
            print ("Produced", num)
            condition.notify()      #waits for 
            condition.release()
                                    #end of Critical section
            time.sleep(1)


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
                                        #start of Critical section
            condition.acquire()
            if not queue:               #if queue is empty
                print ("Nothing in queue, consumer is waiting")
                condition.wait()        #waiting until notified from producer class
                print ("Producer added something to queue and notified the consumer")
            num = queue.pop(0)  
            print ("Consumed", num)
            condition.notify()
            condition.release()
                                        #end of critical section
            time.sleep(1)


ProducerThread().start()
ConsumerThread().start()