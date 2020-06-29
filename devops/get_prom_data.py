from prometheus_http_client import Prometheus 
import prometheus_http_client
from prometheus_http_client.prometheus import *
import os

os.environ['PROMETHEUS_URL'] = 'http://demo.robustperception.io:9090/'
@prom
def up(*args, **kwargs):
    pass
@relabel('100 - (avg by (instance, job) (irate(node_cpu{mode="idle"}[5m])) * 100)')
def hello(*args,**kwargs):
    pass
if __name__ == '__main__':
    print("Up metrics ::",up())
    print("Node CPU Metrics :",hello())
    print("UP With Range ::")
    p = Prometheus()
    print(p.query_rang(metric="up", start=1570221677, end=1570225677))
    print(p.label_values('job'))
    print(dir(Prometheus))
