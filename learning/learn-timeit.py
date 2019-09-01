import timeit

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
	print(timeit.timeit(stmt="list_add()",setup="from __main__ import list_add",number=1000))
	print(timeit.repeat(stmt="list_add()",setup="from __main__ import list_add",repeat=3,number=1000))
	t1 = timeit.Timer(stmt="list_list()",setup="from __main__ import list_list")
	t2 = timeit.Timer(stmt="list_list()",setup="from __main__ import list_list")
	print(t1.timeit(number=1000))
	print(t2.repeat(repeat=3,number=1000))


##python -m timeit   -n 1000 -r 5 -u usec -p  -s 'text = "sample string"; char = "g"'  'char in text'
##
