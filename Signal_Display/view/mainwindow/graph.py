# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:05:19 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.clearlayout import CLEARLAYOUT

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
     
def GRAPH(x,y,layout,a):
    CLEARLAYOUT(layout)
    canvas = FigureCanvas(Figure())
    layout.addWidget(canvas)
    axes = canvas.figure.subplots()
    if a == 1:
        axes.plot(y)
    elif a == 2:
        axes.plot(x,y)
        axes.set_xlabel("Time (s)")
        axes.set_ylabel("Amplitude")
        axes.set_title("Amplitude Vs Time")  
    elif a == 3:
        axes.plot(y)
        axes.set_yscale("log")
    elif a == 4:
        axes.plot(x,y)
        axes.set_xlim(left=0)
        axes.set_yscale("log")
        axes.set_xlabel("Frequency (Hz)")
        axes.set_ylabel("Power spectral density")
        axes.set_title("Frequency Vs Power spectral density")