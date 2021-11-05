# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:13:59 2020

@author: Carlos Mateo Jurado Díaz
"""

from PyQt5 import QtWidgets, uic

class SAMPLINGRATE(QtWidgets.QMainWindow):
    def __init__(self):
        super(SAMPLINGRATE, self).__init__()
        uic.loadUi('view/samplingrate/samplingrate.ui', self)