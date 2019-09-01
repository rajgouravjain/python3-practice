from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from random import randint
from queue import Queue
import threading

import time

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def workerFib(n):
    print(n,fib(n))
    #print(threading.currentThread().getName())

if __name__ == '__main__':
    q = Queue(maxsize=100)
    i = 0
    while not q.full():
        r = randint(0, 34)
        print("Random Item", r,i)
        q.put(r,block=False, timeout=4)
        i += 1
    else:
        print("Queue is Full")


    with ThreadPoolExecutor(max_workers=5) as executor:
        while not q.empty():
            item = q.get(block=False, timeout=1)
            print("Item is:", item)
            executor.submit(workerFib,item)




