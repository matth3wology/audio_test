import wave
import numpy as np
import matplotlib.pyplot as plt
import peakutils

#Open Wave File
f = wave.open('shot.wav','r')

#Convert audio data to Int16 Matrix
data = f.readframes(-1)
data = np.fromstring(data,'Int16')
time = len(data)/44100
x = np.linspace(0,time,len(data))

#Detect Peaks
peaks = peakutils.indexes(data,min_dist=2000)
x_peaks = x[peaks]
y_peaks = data[peaks]

#Plot graph
for i in range(len(peaks)):
    print("Peaks found at time: ",x[peaks[i]]," seconds.")

plt.plot(x_peaks,y_peaks,'rd')
plt.plot(x,data)
plt.show()
