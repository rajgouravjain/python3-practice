import asyncio

async def producer(conf: dict, metric: str ,queue: asyncio.Queue):
    for app in  conf['rules']:
        print(app)
        for rule in conf['rules'][app]:
            if rule['type'] == metric :
                await queue.put((app, rule))

async def consumer(queue: asyncio.Queue):
    while True:
        app , rule  = await queue.get()

        ##Perform analytics here
        #type_map(rule['type'])()

        print(app, rule)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

async def run_engine(conf: dict):
    latency_queue = asyncio.Queue()
    ##asyncio.create_task(producer('latency',latency_queue))

    error_rate_queue = asyncio.Queue()
    ##asyncio.create_task(producer('latency',latency_queue))

    throughput_queue = asyncio.Queue()

    producers = [asyncio.create_task(producer(conf,m, q)) for m,q in zip(("latency","error_rate","throughput"),(latency_queue,error_rate_queue,throughput_queue))]
    consumers = [asyncio.create_task(consumer(q)) for q in (latency_queue,error_rate_queue,throughput_queue)]
    #await asyncio.gather(producer(conf,'latency',latency_queue),producer(conf,'error_rate',error_rate_queue),producer(conf,'throughput',throughput_queue),consumer(latency_queue),consumer(error_rate_queue))
    await asyncio.gather(*producers)
    await latency_queue.join()
    await throughput_queue.join()
    await error_rate_queue.join()
    for c in consumers:
        c.cancel()