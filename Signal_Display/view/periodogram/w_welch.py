# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:13:59 2020

@author: Carlos Mateo Jurado Díaz
"""

from PyQt5 import QtWidgets, uic

class W_WELCH(QtWidgets.QMainWindow):
    def __init__(self):
        super(W_WELCH, self).__init__()
        uic.loadUi('view/periodogram/welch.ui', self)