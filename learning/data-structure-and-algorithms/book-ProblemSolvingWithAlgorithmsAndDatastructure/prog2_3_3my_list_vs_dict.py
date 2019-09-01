import timeit
import random
import matplotlib.pyplot as plt

x =range(10000,250001,10000)
tl = []
td = []
for i in x:
    print i
    l = list(range(i))
    t1 = timeit.Timer("random.randrange(%d) in l "%i, "from __main__ import l; import random")
    tl.append(t1.timeit(number=1000))

    d = {j:None for j in range(i)}
    t2 = timeit.Timer("random.randrange(%d) in d"%i, "from __main__ import d,random")
    td.append(t2.timeit(number=1000))

plt.figure()

# plt.subplot(211)
plt.plot(x,tl,label = "List")
# plt.legend()

# plt.subplot(212)
plt.plot(x,td,label = "Dict")
plt.legend()

plt.show()
