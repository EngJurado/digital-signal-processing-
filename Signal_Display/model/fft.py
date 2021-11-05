# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:48:06 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.graph import GRAPH

from scipy.fft import fft, fftfreq

def FFT(frequency,sr,y,f):
    yfft = fft(y)
    if sr == 0:
        GRAPH(f,yfft,frequency,3)
    else:
        f = fftfreq(y.shape[0], 1/sr)
        GRAPH(f,yfft,frequency,4)
    return f, yfft