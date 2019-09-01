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

def Consumer(q):

    while not q.empty():
        print("Consuming inputs")
        n = q.get(block=False,timeout=1)

        print("Input job is :", n," Output of Job is : ",fib(n), "")
        print(threading.currentThread().getName())

def Producer(q):
    print(threading.currentThread().getName())
    i=0
    while not q.full():
        r = randint(0, 34)
        print("Random Item", r, i)
        q.put(r, block=False, timeout=4)
        i += 1
        print("Submitted ", i + 1, " Jobs by Thread", threading.currentThread().getName())
    else:
        print("Queue is Full")

if __name__ == '__main__':
    q = Queue(maxsize=20)
    max_jobs=100
    jobs = 0


    while  jobs < max_jobs :
        while not q.empty():
            time.sleep(1)
        with ThreadPoolExecutor(max_workers=2) as ce:
            ce.submit(Producer,q)
            ce.submit(Producer, q)

        with ThreadPoolExecutor(max_workers=5) as pe:
            pe.submit(Consumer, q)
            pe.submit(Consumer, q)
            pe.submit(Consumer, q)
            pe.submit(Consumer, q)
        print("Total jobs completed:", jobs)
        jobs += 20




