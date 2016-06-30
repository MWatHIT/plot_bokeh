#!/usr/bin/python
#coding:utf-8
from numpy import arange
from bokeh.plotting import figure, output_file, show
from bokeh.models import FixedTicker


x = [800,10000]
y = [90,90]



output_file("ce101_5.html")

# create a new plot with a log axis type
p = figure(plot_width=600, plot_height=400,
           x_axis_type="log",y_range=(70,130),
           x_range=(100,10000))
# main line
p.line(x, y, line_width=2)
# dash line
p.line([800,800],[0,90],line_dash=(5,5),line_color="black")
# p.line([100,10000],[92,92],line_dash=(5,5),line_color="black")
# p.line([10,25],[95,95],line_dash=(5,5),line_color="black")
# axis Fixed
p.xaxis.ticker=FixedTicker(ticks=[100,800,1000,10000])
# p.yaxis.ticker=FixedTicker(ticks=[70,80,90,92,100,110,120,130])


p.text
p.title = "水面舰船-400Hz-曲线2"
p.xaxis.axis_label = '频率（Hz）'
p.yaxis.axis_label = '限值（dBμA）'


show(p)
