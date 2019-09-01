import sys
import os

def BubbleSortAscendingOrderSortFromHighIndex(array):
    for i in range(len(array)-1,0,-1):
        print "I:", i
        for j in range(0,i):
            print "J:", j
            if array[j+1] < array[j]:
                #swap(array[j+1], array[j])
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            else :
                pass
    print array

if  __name__ == '__main__':
    BubbleSortAscendingOrderSortFromHighIndex([7,6,9,6,8,7,5,10])
