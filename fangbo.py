#!/usr/bin/python
#coding:utf-8
from bokeh.plotting import figure, output_file, show
from bokeh.models import FixedTicker
from numpy import arange

x = arange(0,36,1)
y = [0,0.5,4.8,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4.8,0.5,0]
output_file("fangbo.html")


p = figure(plot_width=400, plot_height=400)
p.line(x,y)

show(p)
