from timeit import Timer

def  test_concate():
    l = []
    for i in range(1000):
        l = l + [i]
def test_append():
    l = []
    for i in range(1000):
        l.append(i)
def test_comprehension():
    l = [ i for i in range(1000) ]

def test_list():
    l = list(range(1000))

if __name__ == "__main__" :
    t1 = Timer("test_concate()", "from __main__ import test_concate")
    print ("Concat", t1.timeit(number=1000),"milliseconds")

    t2 = Timer("test_append()", "from __main__ import test_append")
    print ("Append", t2.timeit(number=1000),"milliseconds")

    t3 = Timer("test_comprehension()", "from __main__ import test_comprehension")
    print ("Comprehension", t3.timeit(number=1000),"milliseconds")

    t4 = Timer("test_list()", "from __main__ import test_list")
    print ("List", t4.timeit(number=1000),"milliseconds")
