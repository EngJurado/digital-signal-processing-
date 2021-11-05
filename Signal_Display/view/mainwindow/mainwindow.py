# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:31:22 2020

@author: Carlos Mateo Jurado Díaz
"""

from PyQt5 import QtWidgets, uic

class MAINWINDOW(QtWidgets.QMainWindow):
    def __init__(self):
        super(MAINWINDOW, self).__init__()
        uic.loadUi('view/mainwindow/mainwindow.ui', self)
        self.t = 0
        self.y = 0
        self.f = 0
        self.yfft = 0
        self.sr = 0
        self.fft = 0
        self.windowsize = 0
        self.overlap = 0