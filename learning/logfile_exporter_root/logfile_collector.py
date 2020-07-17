from prometheus_client import start_http_server, Metric, REGISTRY
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily
import json
import requests
import sys
import time
import fire

class LogFileCollector(object):
  def __init__(self,filename,N):
    self.filename = filename
    self.N = N

   
  def collect(self):
    with open(self.filename,'r') as fp:
      lines = []
      while len(lines) <= self.N: 
            try: 
                fp.seek(-pos, 2) 
          
            except IOError: 
                fp.seek(0) 
                break
              
            finally: 
                lines = list(fp)
                last_seek_pos = fp.tell() 
            pos *= 2
    lines = lines[-self.N:] 
    yield from self.parse_lines(lines)

  def parse_lines(self,lines):
          for line in lines:
            key,value = line.split("=")
            metric = Metric(key, key, 'gauge')
            metric.add_sample(key,value=int(value.rstrip()), labels={})
            yield metric

if __name__ == '__main__':
  fire.Fire(LogFileCollector)
