#!/bin/python3

import math
import os
import random
import re
import sys

## n=10
## f(10) = 2 + f(8)
## f(8) = 3 + f(5)
## f(8) = 2 + f(6)
# Complete the getWays function below.
#memoization_dict = None
memoization_dict = {}


# def getWays(n, c):
#     global memoization_dict
#     for e in c:
#         if n == e:
#             return 1
#         elif n < e:
#             return 0
#         else :
#             if n in memoization_dict.keys():
#                 return memoization_dict[n]
#             else :
#                 op = getWays(n - e, c)
#                 if op:
#                     memoization_dict[n] = op + 1
#                     return memoization_dict[n]
#                 else:
#                     return op
class DAGNode(object):
    def __init__(self,value,child,element):
        self.value = value
        self.children = child or set()
        self.path = {}
        self.path[child] = set()
        self.path[child].add(element)

    def merge(self,node=None):
        if not node == None:
            if self.value == node.value :
                c_diff = self.children.difference(node.children)

                if c_diff:
                    self.children.add(node.children)
                    for c in c_diff:
                        self.path[c] = set()
                        self.path[c].add(node.path[c])

class DAGTree(object):
    def __init__(self,size):
        self.tree =  [0] * (size+1)
    def add_node(self,node):
        self.tree[node.value] = node




def getWays(n,c):
    global memoization_dag
    for e in c:
        if n == 0:
            if not memoization_dag.tree[e]:
                t_node = DAGNode(n,None,e)
                #print(t_node)
                memoization_dag.add_node(t_node)
                memoization_dag.tree[e]

        elif n < 0:
            continue
        else :

            getWays(n-e,c)

            if memoization_dag.tree[n-e] :
                new_c_node = memoization_dag.tree[n-e].merge(memoization_dag.tree[n-e])
                memoization_dag.tree[n-e] = new_c_node

                parent_node = DAGNode(n,new_c_node,e)
                memoization_dag.tree[parent_node.value] = parent_node

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "./out-coin-change-1.txt"
    os.environ['INPUT_PATH'] = "./in-coin-change-1.txt"
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ifptr = open(os.environ['INPUT_PATH'],'r')

    nm = ifptr.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, ifptr.readline().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    print(n,m,c)
    #ways = getWays(n, c)
    memoization_dag = DAGTree(n)
    ways = getWays(n, c)
    print(memoization_dag.tree)
    fptr.write(str(memoization_dag.tree))

    fptr.close()
