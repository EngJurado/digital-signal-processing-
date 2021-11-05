# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:12:15 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.graph import GRAPH

from scipy.signal import welch
from numpy import zeros

def WELCH(frequency,sr,y,windowsize, overlap):
    c = y.shape[1]
    a = int(windowsize/2)
    yfft = zeros((a + 1, c))
    f = zeros((a + 1, c))
    for i in range(c):
        f[:,i], yfft[:, i] = welch(y[:,i],sr,'hanning',windowsize, overlap)
    GRAPH(f,yfft,frequency,4)
    return f, yfft