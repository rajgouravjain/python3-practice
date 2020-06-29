from collections import Counter, Container

"""https://codeshare.io/5z6qVO
1) 2d array, only 0s and 1s, 0s on left and 1s on right in each row
-- find row with max 0s
(m rows, n columns)
Python :: 

a  = [ ["0", "0", "1" , "1"], ["0","1","1","1"] ]

l[0] = 2
l[1] = 1
max(l)
TimeComplexity : m/E[X] * log2n
where  X = random variable for presence of number of zeros in a row
E[X] is Expectation value of X

a[0].index(1)
"""

a = [[0, 0, 0, 1, 1],[1,1,1,1,1],[0,0,0,0,0], [ 0, 1, 1, 1, 1]]


def BinarySearch(l,low,hi):
    print("-----------------------")

    v = (low + hi) // 2
    print(l,low, hi, v)
    if (v == 0):
        return 1-l[v]
    if v == len(l)-1:
        if l[v] == 0:
            return len(l) -1
        else :
            return 0

    if   low != hi:

        if ( l[v] == 0 and l[v + 1] == 1):
            print("Got it!!!")
            return v+1
        elif ( l[v] == 1 and l[v + 1] == 1) :
            print("Left Search")

            return    BinarySearch(l,low,v)

        elif (l[v] == 0 and l[v + 1] == 0) :
            if (v != len(l)-2):
                print("Right Search")
                return  BinarySearch(l,v,hi)
            else :
                return v + 2
        else:
            print("This is impossible case")
            return 0



result = Counter()

i=0

for row in a:
    print("Binary search result", BinarySearch(row,0,len(row)-1))
    result[i] = BinarySearch(row,0,len(row)-1)
    i += 1

print("============Final result=========")
print(result.most_common(1))
