__author__ = 'rjain'

t = [ 9,8,2,7,3,2,6,9,2,1]
def selection_sort(seq):
    for i in range(len(seq) -1, 0, -1):
        max_j = i
        for j in range(max_j):
            if seq[j] > seq[max_j]:
                max_j = j
                seq[i], seq[max_j] = seq[max_j], seq[i]
    return seq

print selection_sort(t)