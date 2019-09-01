__author__ = 'rjain'

t = [ 4,5,2,5,7,6,3,8,9,4,8,3,9,7]
def insersionSort(t):
    for i in range(1,len(t)):
        j=i
        while j>0 and t[j-1] > t[j]:
            t[j-1], t[j] = t[j],t[j-1]
            j -= 1

    return t

print insersionSort(t)

def insersionSortRec(t,i = None):
    if i == None: i = len(t) - 1
    if i == 0: return 0
    insersionSortRec(t,i-1)
    j=i
    while j > 0 and (t[j] <  t[j-1]):
        t[j] , t[j-1] = t[j-1], t[j]
        j -= 1
    return t

print insersionSortRec(t)