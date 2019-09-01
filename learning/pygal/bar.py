#!/usr/bin/python

import pygal

xxdata = []
xdata = []

infile=open('1.txt','r')
for data in infile:
	xdata.append(int(data.rstrip()))
bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.add('Random', xdata)  # Add some values
bar_chart.render_to_file('http-response.svg')
