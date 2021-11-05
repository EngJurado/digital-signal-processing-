# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:38:13 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.graph import GRAPH
from model.settime import SETTIME

from scipy.fft import fftfreq

def PUTSR(time,sr,y,frequency,yfft,fft):
    t=SETTIME(y,sr)
    GRAPH(t,y,time,2)
    if fft == 1:
        f = fftfreq(y.shape[0], 1/sr)
        GRAPH(f,yfft,frequency,4)
    return t