#!/usr/bin/python
#coding:utf-8
from numpy import arange
from bokeh.plotting import figure, output_file, show
from bokeh.models import FixedTicker


x = [25,2600,10000]
y = [95,95,76]



output_file("ce101_1.html")

# create a new plot with a log axis type
p = figure(plot_width=400, plot_height=300,
           x_axis_type="log",y_range=(60,110),
           x_range=(10,10000))
# main line
p.line(x, y, line_width=2)
# dash line
p.line([25,25],[0,95],line_dash=(5,5),line_color="black")
p.line([2600,2600],[0,95],line_dash=(5,5),line_color="black")
p.line([10,25],[95,95],line_dash=(5,5),line_color="black")
# axis Fixed
p.xaxis.ticker=FixedTicker(ticks=[10,25,100,1000,2600,10000])
p.yaxis.ticker=FixedTicker(ticks=[60,70,80,90,95,100,110])


p.text
p.title = "潜艇-DC"
p.xaxis.axis_label = '频率（Hz）'
p.yaxis.axis_label = '基础限值（dBμA）'


show(p)
