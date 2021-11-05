# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:17:48 2020

@author: Carlos Mateo Jurado Díaz
"""

from view.mainwindow.mainwindow import MAINWINDOW
from view.samplingrate.samplingrate import SAMPLINGRATE
from view.mainwindow.clearlayout import CLEARLAYOUT
from view.periodogram.w_welch import W_WELCH
from model.open import OPEN2
from model.putsr import PUTSR
from model.clearsamplingrate2 import CLEARSAMPLINGRATE2
from model.fft import FFT
from model.welch import WELCH

from PyQt5 import QtWidgets
from matplotlib.backends.qt_compat import QtWidgets as pltQtWidgets
import sys
    
app = QtWidgets.QApplication(sys.argv)
main = MAINWINDOW()
main.show()

time = pltQtWidgets.QVBoxLayout(main.viewtime)
frequency = pltQtWidgets.QVBoxLayout(main.viewfrequency)
spectrogram = pltQtWidgets.QVBoxLayout(main.viewspectrogram)

def OPEN():
    main.y = OPEN2(time,main.t)
    CFFT()
    main.sr = 0
    
def SETSAMPLINGRATE():
    main.samplingrate = SAMPLINGRATE()
    main.samplingrate.show()
    main.samplingrate.cancel.clicked.connect(main.samplingrate.close)
    main.samplingrate.ok.clicked.connect(OK)
    
def OK():
    main.sr = main.samplingrate.spinBox.value()
    main.t = PUTSR(time,main.sr,main.y,frequency,main.yfft,main.fft)
    if main.fft == 2:
        SR_WELCH()
    main.samplingrate.close()
    
def CLEARSAMPLINGRATE():
    CLEARSAMPLINGRATE2(time,main.t,main.y,main.fft,main.f,main.yfft,frequency)
    main.sr = 0
    if main.fft == 2:
        CFFT()
    
def PFFT():
    main.f, main.yfft = FFT(frequency,main.sr,main.y,main.f)
    main.fft = 1
    
def PWELCH():
    main.fft = 2
    if main.sr == 0:
        SETSAMPLINGRATE()
    else: 
        SR_WELCH()
        
def SR_WELCH():
    main.w_welch = W_WELCH()
    main.w_welch.show()
    main.w_welch.cancel.clicked.connect(main.w_welch.close)
    main.w_welch.ok.clicked.connect(OK_WELCH)
    
def OK_WELCH():
    main.windowsize = main.w_welch.spinBox.value()
    main.overlap = main.w_welch.spinBox_2.value()
    main.f, main.yfft = WELCH(frequency,main.sr,main.y,main.windowsize, main.overlap)
    main.w_welch.close()
    
def CFFT():
    CLEARLAYOUT(frequency)
    main.fft = 0
         
main.actionOpen.triggered.connect(OPEN)
main.actionSet_sampling_rate.triggered.connect(SETSAMPLINGRATE)
main.actionClear_sampling_rate.triggered.connect(CLEARSAMPLINGRATE)
main.actionFast_Fourier_Transform.triggered.connect(PFFT)
main.actionWelch.triggered.connect(PWELCH)
main.actionDisable_periodogram.triggered.connect(CFFT)
main.actionSe_spectrogram.triggered.connect(PWELCH)
main.actionDisable_spectrogram.triggered.connect(CFFT)

sys.exit(app.exec_())