def spam():
    while True:
        item = yield
        print("Got :", item)

if __name__ == '__main__':
    s = spam()
    next(s)
    s.send("Hello")
    s.send("Bye")

    next(s,"Hey")
