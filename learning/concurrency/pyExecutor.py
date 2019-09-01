from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def workerFib(n):
    print(fib(n))




if __name__ == '__main__':
    t1 = time.time()

    with ThreadPoolExecutor(max_workers=2) as executor:
        ft1 = executor.submit(workerFib, 36)
        ft2 = executor.submit(workerFib, 36)
    print("Thread pool excutor time {}".format(time.time() - t1))

    t2 = time.time()

    with ProcessPoolExecutor(max_workers=2) as executor :
        fp1 = executor.submit(workerFib,36)
        fp2 = executor.submit(workerFib,36)
    print("Process pool executor time {}".format(time.time()-t2))


