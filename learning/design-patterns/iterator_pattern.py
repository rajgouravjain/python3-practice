
l = [ 2, 5,3,6,7,2,7]

for i in l:
    print(i)


iterator = l.__iter__()
print(iterator.__next__())
print(iterator.__next__())



lc = [ n**2 for n in l if n%2 == 1]

print(lc)