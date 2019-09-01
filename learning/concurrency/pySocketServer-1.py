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
while True:
    rec = conn.recv(1024)
    print("Received: ", rec)
    rec = int(rec.decode())

    resp = fib(rec)
    resp = str(resp).encode()
    #print("Response: ", resp)
    conn.sendall(resp)





