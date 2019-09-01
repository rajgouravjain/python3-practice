import sys
import os

def BubbleSort_AscendingOrder_SortFromHighIndex(array):
    for i in range(0,len(array)):
        print "I: ",i
        for j in range(len(array)-1,i,-1):
            print "J: ",j
            if array[j] < array[j-1]:
                #swap(array[j+1], array[j])
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array

if  __name__ == '__main__':
    print BubbleSort_AscendingOrder_SortFromHighIndex([11,6,9,6,8,7,10,12])
