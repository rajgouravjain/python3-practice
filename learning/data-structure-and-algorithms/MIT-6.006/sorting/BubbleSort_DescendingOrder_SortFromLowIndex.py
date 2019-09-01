import os
import sys

def BubbleSort_DescendingOrder_SortFromLowIndex(array):
    for i  in range(len(array)):
        for j in range(len(array)-1,i,-1):
            if array[j] > array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array

if __name__ == '__main__' :
    print BubbleSort_DescendingOrder_SortFromLowIndex([2,4,62,6,2,668,8,3,-10])
