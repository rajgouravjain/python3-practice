from multiprocessing import Pool, Process, Manager, Barrier, Array, Queue

def producer(q,work):
    print("In Producer")

    if not q.full():
        q.put(work)


def consumer(q):
    print("In Consumer")
    if not q.empty():
        result = q.get()
        print(result)

if __name__ == '__main__':
    q = Queue(maxsize=2)
    print(q)
    p1 = Process(target=producer,args=(q,),kwargs={"work": "HI"})
    p2 = Process(target=producer,args=(q,"Hello"))

    c1 = Process(target=consumer,args=(q,))
    c2 = Process(target=consumer,args=(q,))

    p1.start()
    p2.start()

    c1.start()
    c2.start()



