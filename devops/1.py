import os
import itertools
import subprocess
import sys
print(os.path.dirname('/usr/local/1.py'))
print(os.path.basename('/usr/local/1.py'))
print(os.strerror(100))

print(set(map(lambda x,y : x + y, [1,2,3,4,5,6], [6,5,4,3,2,1])))
print(itertools.product(["Hello","World"], ["How", "Are", "you"]))

s = subprocess.run(['ls', '-al', '/dev/nurll'], stdout= subprocess.PIPE, stderr = subprocess.PIPE)
print(s.returncode,s.stdout.decode('utf-8'), "ERROR:", s.stderr.decode('utf-8'))

#with  subprocess.Popen(["ls"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True) as p1:
#    print("Popen output for subprocess with PID:", p1.pid)
#    for l in (s.decode("utf-8").strip() for s in p1.stdout.readlines()):
#        print(l)
#    print("===================================")

with subprocess.Popen(['tail', '-10', '/var/log/system.log'], stdout= subprocess.PIPE) as p1:
    with subprocess.Popen(['grep','-i','user'], stdin=p1.stdout , stdout=subprocess.PIPE) as p2:
        for l in (line.decode('utf-8').strip() for line in p2.stdout.readlines()):
            print(l)


