import threading
from threading import Thread , Lock, RLock, Condition, Timer, Semaphore, BoundedSemaphore
from queue import Queue
from random import randint

import sys

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


threadLock = Lock()
threadCondition = Condition(threadLock)


def worker_fib(n):
       with  threadCondition:
            print("current enumerate state is : {}".format(threading.enumerate()))
            print("Thread Count: {}".format(threading.activeCount()))
            print("Thread status: {}".format(threading.currentThread()))
            print(fib(n))

if __name__ == '__main__':
    q = Queue(maxsize=20)
    i=0
    while not q.full():
        r = randint(0, 34)
        print("Random Item", r,i)
        q.put(r,block=False, timeout=4)
        i += 1
    else:
        print("Queue is Full")


    #with threadCondition :
    while not q.empty():
        item = q.get(block=False, timeout=1)
        print("Item is:", item)
        Thread(target=worker_fib, args=(35,)).start()

