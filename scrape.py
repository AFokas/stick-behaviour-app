
#!/bin/python
from bokeh.embed import file_html
from bokeh.resources import CDN
import sys
import re
import urllib2
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
from bokeh.plotting import figure, output_file, show
args = []
with open('tmp.txt') as f:
    args = f.read().splitlines()


ticker  = args[0]
cols = []
plot_date = []
cols.append('ticker')
cols.append('date')
if 'cp' in args:
    cols.append('close')
    plot_date.append('close')
if 'op' in args:
    cols.append('open')
    plot_date.append('open')
if 'cap' in args:
    cols.append('adj_close')
    plot_date.append('adj_close')
if 'oap' in args:
    plot_date.append('adj_open')
    cols.append('adj_open')

df = pd.read_csv('df_2017.csv',parse_dates = ['date'])

# In[17]:

open_close = df[cols]
pd.options.display.max_rows = 3000


# In[21]:

to_plot = open_close[open_close.ticker=='%s'%ticker]
del to_plot['ticker']


# In[25]:

#output_file("datetime.html")
from bokeh.palettes import Spectral11

# create a new plot with a datetime axis type
numlines = len(plot_date)
#import color pallet

from random import shuffle
shuffle(Spectral11)
mypalette = Spectral11[0:numlines]
p = figure(width=800, height=250, x_axis_type="datetime")
p.xaxis.axis_label = 'Date'
for (columnnames, colore) in zip(plot_date, mypalette):
    p.line(to_plot.date, to_plot[columnnames], legend = columnnames, color = colore )

show(p)

html = file_html(p,CDN, "Stock Data")
f=open('templates/load_network.html','w')
for line in html:
    f.write('%s'%line)
f.close()


