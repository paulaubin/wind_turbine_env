#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# Created By  : Paul Aubin
# Created Date: 2022/09/26
# ----------------------------------------------------------------------
""" Digital butterworth filter """
# ----------------------------------------------------------------------

import numpy as np
from scipy.signal import butter, lfilter, freqz

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def manual_filter(b, a, input, init=[]):
    """Manually computes a digital filter.

    Keyword arguments:
    b -- the numerator of a filter [double]
    a -- the denominator of a filter [double]
    input -- the data to be filtered [np.array]
    init -- the initial values of the filter [np.array]

    Output:
    y -- the filtered values of input

    ex : 
    x.pop(0)
    x.append(update_x())
    yf = manual_filter(b, a, x, y[1:]) to calculate x filtered with lists of size order + 1
    y.pop(0)
    y.append(yf[-1])
    """
    order = len(a)
    y = np.array(np.zeros(len(input)))
    if len(init) == 0:
        init = np.array(np.zeros(order))
    for i in range(0, len(input)):
        if i>= order - 1:
            x_term = np.sum(b * np.flip(input[i-order+1:i+1]))
            y_term = np.sum(a[1:] * np.flip(y[i-order+1:i]))
            y[i] = 1/a[0] * (x_term - y_term)
        else:
            y[i] = init[i]
    return y 
