import threading
from threading import Lock
from threading import Thread
from threading import Condition
from threading import RLock
from threading import Semaphore
from threading import BoundedSemaphore

thLock = Lock()

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def workerFib(n):
    thLock.acquire()
    print(" I am {}".format(threading.currentThread().getName()))
    print("Active thread count is : {}".format(threading.activeCount()))
    print("current enumerate state is : {}".format(threading.enumerate()))
    print(fib(n))
    thLock.release()



#print fib(5)
t1 = Thread(target=workerFib, args=(20,) ,name='f20')
t2 = Thread(target=workerFib,args=(30,), name='f30')

t1.start()
t2.start()
print(t1.isAlive())
print(t2.isAlive())

