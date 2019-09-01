import os
import sys

def BubbleSort_DescendingOrder_SortFromHighIndex(array):
    for i  in range(len(array)-1,0,-1):
        for j in range(0,i):
            if array[j+1] > array[j]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

if __name__ == '__main__':
    sorted_array = BubbleSort_DescendingOrder_SortFromHighIndex([23,4,0,-10,45,3])
    print sorted_array
