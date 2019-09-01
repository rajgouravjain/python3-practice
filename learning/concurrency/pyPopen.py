from subprocess import Popen, PIPE, call, check_call, check_output
import sys
with  Popen(["dir"],stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True) as p1:
    print("Popen output for subprocess with PID:", p1.pid)
    for l in (s.decode("utf-8").strip() for s in p1.stdout.readlines()):
        print(l)
    print("===================================")
try :
    retcode = call("dir",stdout=sys.stdout,stderr=sys.stdout,shell=True)
    if not retcode:
        print("Execute Return code", retcode)
        print("This code will also be printed")
except :
    print("Exception is ",file=sys.stderr)
