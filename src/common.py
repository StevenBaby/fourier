# coding=utf-8

'''
(C) Copyright 2021 Steven;
@author: Steven kangweibaby@163.com
@date: 2021-10-24
'''

import pyaudio
import math

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024


A0 = 27.5
A1 = 55
A2 = 110
A3 = 220

A4 = 440
A5 = A4 * 2
A6 = A4 * 4
A7 = A4 * 4

C4 = 261.63
C8 = 4186.0
