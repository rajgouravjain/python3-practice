from subprocess import Popen, PIPE, run
import sys
import shlex

print(sys.version)
print(sys.version_info)



p0 = run(['ls', '-al'],capture_output=True, timeout=0.1, check=False)
#print(str(p0.stdout,'utf-8') )

with  Popen(['ls'], bufsize=-1, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, shell=False) as p1:
    with Popen(['grep','-e',"^-rwx\|py"], bufsize=-1, executable=None, stdin=p1.stdout, stdout=PIPE, stderr=PIPE, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), encoding=None, errors=None, text=None) as p2:
        for l in p2.stdout.readlines():
            print(str(l.rstrip(),'utf-8'))

s1 = "ls"
s2 = 'grep -e "^max.*py$"'
s3 = "xargs ls -al"

print(shlex.split(s2))
with Popen(shlex.split(s1),stdin=PIPE,stdout=PIPE,stderr=PIPE,bufsize=10,close_fds=True) as p3:
    with Popen(shlex.split(s2), stdin=p3.stdout,stdout=PIPE, stderr=PIPE) as p4:
        with Popen(shlex.split(s3),stdin=p4.stdout,stdout=PIPE,stderr=PIPE) as p5:
            for line in p5.stdout.readlines():
                print(str(line.rstrip(),'utf-8'))
        print(p5.returncode)
    print(p4.returncode)
print(p3.returncode)

c1 = "ls -alrt"
with Popen(shlex.split(shlex.quote(c1)),stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True) as p6:
    for line in p6.stdout.readlines():
        print(str(line.rstrip(),'utf-8'))
    for line in p6.stderr.readlines():
        print(str(line.rstrip(),'utf-8'))
print(p6.returncode)
