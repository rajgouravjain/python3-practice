""" given an array find two number such that sum is equal to k"""

a  = [1,3,5,7,8,5,3,5,7,3,2]

k = 8

sorted_a = a.sorted()
##sorted_a = [0,1,2,3,4,5,6,7,8,9]

i_max = len(sorted_a)

i_max = sorted_a.index(k)

if min(sorted_a) > k :
    print("Solution not possible")

for i in range(i_max+1):
    for j in range(i+1,i_max+1) :
        if  ( sorted_a[i] + sorted_a[j] == k) :
            print(sorted_a[i], sorted_a[j])



