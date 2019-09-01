import os
import datetime
import pandas as pd
import re
import sys


print(sys.getdefaultencoding())


if __name__ == '__main__':
    log_list = None
    log_list = []
    with open('/Users/user/1.log', 'r') as fd:
        for line in fd:
            print(line)
            m = re.search(
                '\[2018-07-23 (?P<log_time>\d{2}:\d{2}:\d{2})\] \[(?P<java_thread>[a-zA-Z0-9_-]+)\] (?P<log_level>[a-zA-Z0-9]+)  (?P<class>[a-zA-Z0-9._-]+) \- (?P<msg>.+)',
                line)
            if not m:
                print("NO MATCH")
                pass
            else:
                print(m.groupdict())
                log_list.append(m.groupdict())




