from  timeit import Timer
import matplotlib.pyplot as plt
tz = []
te = []
x = range(10000,1000001,10000)
for i in x:
    print i
    l = list(range(i))
    ##Create Timer object with Statement and Setup
    t1 = Timer(stmt="l.pop(0)", setup="from __main__ import l")
    l = list(range(i))
    t2 = Timer("l.pop()", "from __main__ import  l")

    tz.append(t1.timeit(number=1000))
    te.append(t2.timeit(number=1000))

plt.figure()
plt.subplot(211)
plt.plot(x,tz, label="Pop(0)")
plt.legend()
plt.subplot(212)
plt.plot(x,te, label="Pop")
plt.legend()
plt.show()
