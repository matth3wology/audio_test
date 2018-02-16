#!/bin/python
import wave
import numpy as np
import matplotlib.pyplot as plt

m = wave.open('440.wav','r')
frames = m.readframes(-1)
frames = np.fromstring(frames,"Int16")

channels = [[] for channel in range(2)]

for a,b in enumerate(frames):
	channels[a%2].append(b)

signal = channels[0]
time = len(signal)/44100
x=np.linspace(0,time,len(signal))

plt.plot(x,signal)
plt.show()



