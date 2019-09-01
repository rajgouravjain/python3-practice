__author__ = 'rjain'

t = [9,8,2,7,3,2,6,9,2,1]
def InsertionSortAscFromEnd(t):
    """
    For a given value of i sort all the number and move ahead and sort again.
    I.e For a given value of i, bring t[i] to left most position
    :param t:
    :return:

    """
   for i in range(1,len(t)):
        for j in range(i,0, -1):
            if t[j] < t[j - 1]:
                t[j - 1],t[j] = t[j], t[j - 1]
    return t

print InsertionSortAscFromEnd(t)

print range(10,2, -1)