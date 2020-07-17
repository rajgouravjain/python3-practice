#!/usr/bin/env python3

import os
import time
import prometheus_client

from datetime import date
from flask import Response, Flask, request
from prometheus_client import Gauge

app = Flask(__name__)

graphs = {}
graphs['byterate'] = Gauge('byterate', 'Collects response byte-rate', ["app"])
graphs['overlap'] = Gauge('overlap', 'Collects request overlap', ["app"])

def get_logfile_path(filepath='/usr/local/scene7'):
	paths = []
	filetype = "statistics-{}.log".format(date.today())
	for root, dirs, files in os.walk(filepath):
		for file in files:
			if file.lower().startswith(filetype.lower()):
				paths.append(os.path.join(root, file))
	return (paths)


def parse_logs():
	files = get_logfile_path()
	f = open(files[0], "r")
	f.seek(0, 2)
	line = f.readline()
	if line: yield line

@app.route("/")
def hello():
    return "Welcome to Prometheus World!! Use /metrics to fetch Metrics"
@app.route("/metrics")
def requests_count():
   metrics =  parse_logs()
   for line in metrics:
     col = line.split()
     if 'ovlp' in col:
       pass
     else:
       graphs['byterate'].labels(app='cs-live').set(col[3])
       graphs['overlap'].labels(app='cs-live').set(col[4])
   res = []
   for k,v in graphs.items():
     res.append(prometheus_client.generate_latest(v))
   return Response(res, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9191)
