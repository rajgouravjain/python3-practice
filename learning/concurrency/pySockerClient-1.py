import socket
import time
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1",25000))

req = str(10).encode()
#print("Request : ", req)
n=0
while True:
    t1 = time.time()
    while n < 10000:

        #print(c,req)
        c.sendall(req)
        #result = c.recv(100)
        n +=1
    print(time.time()- t1, "sec")
    n=0
c.close()