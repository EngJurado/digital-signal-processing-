# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:06:33 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.graph import GRAPH

from numpy import loadtxt
from PyQt5.QtWidgets import QFileDialog
from scipy.signal import detrend

def OPEN2(time,t):
    file, _ = QFileDialog.getOpenFileName()
    y = loadtxt(file, comments="%", delimiter=",", usecols=(1, 2, 3, 4, 5, 6, 7, 8))
    y = detrend(y,0)
    GRAPH(t,y,time,1)
    return y