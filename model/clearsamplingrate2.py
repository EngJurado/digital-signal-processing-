# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:57:08 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.graph import GRAPH

def CLEARSAMPLINGRATE2(time,t,y,fft,f,yfft,frequency):
    GRAPH(t,y,time,1)
    if fft == 1:
        GRAPH(f,yfft,frequency,3)