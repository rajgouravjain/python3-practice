#Simple example no. 1 of Generator using yield


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def count_down(n):
    print("Start of countdown function")
    while n > 1 :
        yield  fib(35)
        print("Is function suspended")
        n -= 1
        print("N is",n)

if __name__ == '__main__':
    g = count_down(3)
    #print(g)
    print(g.__next__())
    print(g.__next__())
    #print(g.__next__())
    #print(g.__next__())
