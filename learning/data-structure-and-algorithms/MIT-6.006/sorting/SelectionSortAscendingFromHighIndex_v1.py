__author__ = 'rjain'


def selectionSort(t):
        for i in range(len(t)):
            for j in range(i+1,len(t)):
                if t[i] > t[j]:
                    temp = t[i]
                    t[i] = t[j]
                    t[j] = temp
        return t

print   selectionSort([9,2,3,8,4,2,5])

def selectionSort1(t):
    for