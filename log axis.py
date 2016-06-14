#!/usr/bin/python
#coding:utf-8
from numpy import arange
from bokeh.plotting import figure, output_file, show
from bokeh.models import FixedTicker
#from bokeh.models import HoverTool, ColumnDataSource


x = [25,1000,10000]
y1 = [100,100,90]
y2 = [110,110,100]


output_file("log.html")

# create a new plot with a log axis type
p = figure(plot_width=400, plot_height=400,
           x_axis_type="log",y_range=(60,120),
           x_range=(10,10000))

p.line(x, y1, line_width=2)
p.line(x, y2, line_width=2)
p.line([25,25],[0,110],line_dash=(5,5),line_color="black")
p.line([1000,1000],[0,110],line_dash=(5,5),line_color="black")
p.xaxis.ticker=FixedTicker(ticks=[10,25,100,1000,10000])


p.text
p.title = "限值图例子"
p.xaxis.axis_label = '频率（Hz）'
p.yaxis.axis_label = '限值（dBμA）'
#p.circle(x1, y1, fill_color="white", size=8)
#p.circle(x2, y2, fill_color="white", size=8)

#p.select_one(HoverTool).tooltips =["坐标"]


#show(p)
