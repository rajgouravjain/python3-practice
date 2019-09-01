import os

with open('all.txt') as all :
        all_set = {i for i in all}

with open('b_v.txt') as b_v:
        b_v_set = {i for i in b_v}

with open('bv.txt') as bv:
    bv_set = {i for i in bv}


untagged_set = (all_set - b_v_set) - bv_set

print(untagged_set)

for i in untagged_set:
    print(i)