# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:06:48 2021
A simple script that gives users abilty to plot a graph manually and generate
coordinates based on the plot for various purposes.
@author: Tharun Loknath
"""

import matplotlib.pyplot as plt

#Specify figure size
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
#specify your range
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
plt.grid(True)

coords = []

def onclick(event):
    x, y = event.xdata, event.ydata
    
    print(f'{x:0.1f},{y:0.1f}')

    global coords
    coords.append((x, y))

    ax.scatter([x], [y], c='b', s=150)
    plt.draw()
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)

fig.show()