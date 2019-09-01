import os
import json
from itertools import groupby
from operator import itemgetter

rds_class_to_instances_map = json.load(open('/Users/user/1.json'))

final_map = {}

print(rds_class_to_instances_map)



for l in rds_class_to_instances_map:
    print(l)
    if l['Class'] not in  final_map:
        final_map[ l['Class'] ] = [ l['Name'] ]

    else:
        final_map[l['Class']].append(l['Name'])

print(final_map)

