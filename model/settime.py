# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:42:53 2020

@author: Carlos Mateo Jurado Díaz
"""

from numpy import arange

def SETTIME(y,sr):
    x = arange(0,y.shape[0]/sr,1/sr)
    return x