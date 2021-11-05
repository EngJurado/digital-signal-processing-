# -*- coding: utf-8 -*-
"""

Author: Carlos Mateo Jurado Díaz

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as dsp

def open_signal(file, sr):
    """
    Open a txt file where the signal is
    
    Parameters:
        
        file: Address where the file is located
        sr: Sampling rate
        
    Return:
        
        signal: The numpy-shaped signal
        t: Time vector
    
    """

    signal = np.loadtxt(file, comments="%", delimiter=",", usecols=(1, 2, 3, 4, 5, 6, 7, 8))
    c = signal.shape
    c = c[0]
    x = c / sr
    t = np.arange(0, x, 1 / sr)

    return signal, t

def filter_design(sr, locutoff=0, hicutoff=0, revfilt=0):
    """
    Creates the appropriate coefficients for the use of a filtfilt filter 
    with hamming window and a 0.25 Hz transition band. The 
    coefficient is 1
    
    Parameters:
        
        sr: Sampling rate
        
        remove band:
            locutoff: Lower cutoff frequency
            hicutoff: Upper cutoff frequency
            revfilt = 1
            
        pass band:
            locutoff: Lower cutoff frequency
            hicutoff: Upper cutoff frequency
            revfilt = 0
            
        low pass:
            locutoff = 0
            hicutoff: cutoff frequency
            revfilt = 0
            
        high pass:
            locutoff: cutoff frequency
            hicutoff = 0
            revfilt = 1
        
    Return:
        
        b: The numerator coefficient vector of the filter.

    """

    def firws(m, f, w, t=None):

        def fkernel(m, f, w):
            m = np.arange(-m / 2, (m / 2) + 1)
            b = np.zeros((m.shape[0]))
            b[m == 0] = 2 * np.pi * f
            b[m != 0] = np.sin(2 * np.pi * f * m[m != 0]) / m[m != 0]
            b = b * w
            b = b / np.sum(b)
            return b

        def fspecinv(b):
            b = -b
            b[int((b.shape[0] - 1) / 2)] = b[int((b.shape[0] - 1) / 2)] + 1
            return b

        f = np.squeeze(f)
        f = f / 2;
        w = np.squeeze(w)
        if (f.ndim == 0):  # low pass
            b = fkernel(m, f, w)
        else:
            b = fkernel(m, f[0], w)  # band

        if (f.ndim == 0) and (t == 'high'):
            b = fspecinv(b)
        elif (f.size == 2):
            b = b + fspecinv(fkernel(m, f[1], w))  # reject
            if t == None or (t != 'stop'):
                b = fspecinv(b)  # bandpass
        return b

    transitionband = 0.25
    fNyquist = sr / 2
    if hicutoff == 0:
        hicutoff = locutoff
        locutoff = 0
        revfilt = 1
    if locutoff > 0 and hicutoff > 0:
        edgeArray = np.array([locutoff, hicutoff])
    else:
        edgeArray = np.array([hicutoff])
    if np.any(edgeArray < 0) or np.any(edgeArray >= fNyquist):
        return False
    maxBWArray = edgeArray.copy()
    if revfilt == 0:
        maxBWArray[-1] = fNyquist - edgeArray[-1]
    elif len(edgeArray) == 2:
        maxBWArray = np.diff(edgeArray) / 2
    maxDf = np.min(maxBWArray)
    if revfilt == 1:
        df = np.min([np.max([maxDf * transitionband, 2]), maxDf])
    else:
        df = np.min([np.max([edgeArray[0] * transitionband, 2]), maxDf])
    filtorder = 3.3 / (df / sr)
    filtorder = np.ceil(filtorder / 2) * 2
    dfArray = [[df, [-df, df]], [-df, [df, -df]]]
    cutoffArray = edgeArray + np.array(dfArray[revfilt][len(edgeArray) - 1]) / 2
    winArray = dsp.hamming(int(filtorder) + 1)
    if revfilt == 1:
        filterTypeArray = ['high', 'stop']
        b = firws(filtorder, cutoffArray / fNyquist, winArray, filterTypeArray[len(edgeArray) - 1])
    else:
        b = firws(filtorder, cutoffArray / fNyquist, winArray)
    return b


def prefiltered(signal, sr):
    """
    The EEG signal is pre-filtered with a band pass filter between
    0.25 Hz and 50 Hz, the tendency to the signal is removed and 
    an outlier is interpolated
    
    Parameters:
        
        signal: The numpy-shaped signal
        sr: Sampling rate
        
    Return:
        
        filtered: The numpy-shaped prefiltered signal
    
    """

    fil = filter_design(sr, locutoff=0.25, hicutoff=50, revfilt=0)
    filtered = np.zeros(signal.shape)
    c = signal.shape
    c = c[1]

    def normalization(signal):
        signal2 = signal
        x = 2 * np.std(signal, dtype=np.float32)
        for j in np.arange(len(signal)):
            if signal[j] > x:
                signal2[j] = x
            elif signal[j] < (-x):
                signal2[j] = (-x)
        return signal2

    for i in range(c):
        filtered[:, i] = dsp.filtfilt(fil, 1, signal[:, i])
        filtered[:, i] = dsp.detrend(filtered[:, i])
        filtered[:, i] = normalization(filtered[:, i])
        filtered[:, i] = normalization(filtered[:, i])
    return filtered


def periogram(signal, sr):
    """
    The power spectral density of the signal is obtained
    
    Parameters:
        
        signal: The numpy-shaped signal
        sr: Sampling rate
        
    Return:
        
        f: Frequency (Hz)
        power: Power spectral density

    """

    c = signal.shape
    c = c[1]
    power = np.zeros((10 * sr + 1, c))
    for i in range(c):
        f, power[:, i] = dsp.welch(signal[:, i], sr, 'hanning', 20 * sr, 10 * sr)
    return f, power
