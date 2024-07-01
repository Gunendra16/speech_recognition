import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("pro_audio.wav", "rb")

# we will use the following parameters of audio

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples/ sample_freq

print(t_audio)

#now we will try to plot 
signal_array = np.frombuffer(signal_wave, dtype = np.int16)

times = np.linspace(0,5,num = n_samples)

plt.figure(figsize = (5,2))
plt.plot(times, signal_array)
plt.title(" Audio signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim( 0 , 5)
plt.show()

