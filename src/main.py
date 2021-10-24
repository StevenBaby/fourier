# coding=utf-8

'''
(C) Copyright 2021 Steven;
@author: Steven kangweibaby@163.com
@date: 2021-10-24
'''

import pyaudio
import numpy as np
import matplotlib.pyplot as plt


from common import *

i = 0
f, ax = plt.subplots(2)

# Prepare the Plotting Environment with random starting values
x = np.arange(10000)
y = np.random.randn(10000)

# Plot 0 is for raw audio data
li, = ax[0].plot(x, y)
ax[0].set_xlim(0, 1000)
ax[0].set_ylim(-50000, 50000)
ax[0].set_title("Raw Audio Signal")
# Plot 1 is for the FFT of the audio
li2, = ax[1].plot(x, y)
ax[1].set_xlim(A0, C8)
ax[1].set_ylim(-100, 100)
ax[1].set_xscale('log')
ax[1].set_title("Fast Fourier Transform")
# Show the plot, but without blocking updates
plt.pause(0.01)
# plt.tight_layout()


def plot_data(in_data):
    # get and convert the data to float
    audio_data = np.fromstring(in_data, np.int16)

    # Fast Fourier Transform, 10*log10(abs) is to scale it to dB
    # and make sure it's not imaginary
    dfft = 10. * np.log10(abs(np.fft.rfft(audio_data)))

    # Force the new data into the plot, but without redrawing axes.
    # If uses plt.draw(), axes are re-drawn every time
    # print audio_data[0:10]
    # print dfft[0:10]
    # print

    li.set_xdata(np.arange(len(audio_data)))
    li.set_ydata(audio_data)

    li2.set_xdata(np.arange(len(dfft)) * 10.)
    li2.set_ydata(dfft)

    # Show the updated plot, but without blocking
    plt.pause(0.001)


audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

stream.start_stream()

while True:
    try:
        plot_data(stream.read(CHUNK))
    except Exception:
        break

stream.stop_stream()
stream.close()

audio.terminate()
