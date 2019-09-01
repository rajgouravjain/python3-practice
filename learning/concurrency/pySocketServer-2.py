from concurrent.futures import ThreadPoolExecutor

import socket

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(("127.0.0.1",25000))


s.listen(10)
conn, addr = s.accept()
with ThreadPoolExecutor(4) as executor:
    while True:
        req = conn.recv(1024)
        print("Received: ", req)
        req = int(req.decode())

        resp = executor.submit(fib,req)
        print(resp)
        #resp = str(resp).encode()
        #print("Response: ", resp)
        #conn.sendall(resp)





