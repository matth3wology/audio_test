#!/usr/bin/python
import wave
import numpy as np
import matplotlib.pyplot as plt

#Need to get (x,y) coordinates of a DFFT from a wave sample. @matth3wology

#Import wav file to matplot Frequency Domain
m = wave.open("440.wav","r")

#Convert wav to numpy matrix
frames = m.readframes(-1)
frames = np.fromstring(frames,"Int16")

channels = [[] for channel in range(m.getnchannels())]

#Checking the number of channels to take both Mono and Stereo
for a,b in enumerate(frames):
    channels[a%len(channels)].append(b)

signal = channels[0]

N = len(signal)
fft = np.fft.fft(signal)

y = 2.0/N * np.abs(fft[:N//2])
x = np.linspace(0.0,m.getframerate()/2.0,N/2)
plt.plot(x,y)

#Show the plot
plt.show()
