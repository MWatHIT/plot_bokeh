#!/usr/bin/python
#coding:utf-8
from numpy import arange
from bokeh.plotting import figure, output_file, show
from bokeh.models import FixedTicker
from bokeh.models import HoverTool, BoxSelectTool, BoxZoomTool, PanTool


x = [10000,500000,10000000]
y = [94,60,60]



output_file("ce102_1.html")
# add select tool
select = [PanTool(),BoxZoomTool(),BoxSelectTool(),HoverTool()]
# select = [HoverTool()]
# create a new plot with a log axis type
p = figure(plot_width=700, plot_height=400,
           x_axis_type="log",y_range=(40,110),
           x_range=(10000,10000000),tools=select)
# main line
p.line(x, y, line_width=2)
# dash line
p.line([500000,500000],[0,60],line_dash=(5,5),line_color="black")
# p.line([2600,2600],[0,95],line_dash=(5,5),line_color="black")
# p.line([10,25],[95,95],line_dash=(5,5),line_color="black")
# axis Fixed
p.xaxis.ticker=FixedTicker(ticks=[10000,100000,500000,1000000,10000000])
p.yaxis.ticker=FixedTicker(ticks=[40,50,60,70,80,90,94,100,110])


p.text
p.title = "基本限值"
p.xaxis.axis_label = '频率（Hz）'
p.yaxis.axis_label = '限值（dBμA）'


show(p)
