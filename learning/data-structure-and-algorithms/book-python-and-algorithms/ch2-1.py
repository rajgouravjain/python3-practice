import timeit
"""
So we see the following pattern for lists:
Operation Big-O Efficiency
index [] O(1)
index assignment O(1)
append O(1)
pop() O(1)
pop(i) O(n)
insert(i,item) O(n)
del operator O(n)
iteration O(n)
contains (in) O(n)
get slice [x:y] O(k)
del slice O(n)
set slice O(n+k)
reverse O(n)
concatenate O(k)
sort O(n log n)
multiply O(nk)

Big-O Efficiency of Python Dictionary Operations
Operation Big-O Efficiency
copy O(n)
get item O(1)
set item O(1)
delete item O(1)
contains (in) O(1)
iteration O(

"""


def list_add():
    l = []
    for i in range(1000):
        l = l + [i]

def list_append():
    l = []
    for i in range(1000):
        l.append(i)


def list_comprehension():
    l = [i for i in range(1000)]


def list_list():
     l = list(range(1000))

if __name__ == "__main__":
    t1 = timeit.Timer("list_add()", setup = "from __main__ import list_add")
    print("list_add_output",t1.timeit(number=100),"milliseconds")

    t2 = timeit.Timer(stmt="list_append()", setup = "from __main__ import list_append")
    print("list_append_output", t1.timeit(number=100), "milliseconds")

    t3 = timeit.Timer(stmt="list_comprehension()",setup = "from __main__ import list_comprehension")
    print("list_comprehension_output", t3.timeit(number=100),"milliseconds")

    t4 = timeit.Timer(stmt="list_list()", setup = "from __main__ import list_list")
    print("list_list_output", t4.timeit(number=100),"milliseconds")

