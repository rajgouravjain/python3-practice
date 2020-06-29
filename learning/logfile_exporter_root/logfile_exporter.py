from prometheus_client import start_http_server, Metric, REGISTRY
import fire
import json
import requests
import sys
import time
from logfile_collector import LogFileCollector

class FileDataExporter(object):
  def __init__(self,prom_port,metric_url="/metrics"):
    self.prom_port= prom_port
    self.metric_url = metric_url

  def run(self,filename,N=10,slack_channel="slack-api-test"):
    REGISTRY.register(LogFileCollector(filename=filename,N=int(N)))
    start_http_server(int(self.prom_port))
    try:
      while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

    self.shutdown()

  def shutdown(self):
    sys.exit(0)

if __name__ == '__main__':
  fire.Fire(FileDataExporter)
