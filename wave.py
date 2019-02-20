import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('jas122.wav')
print (fs, len(data),data)
plt.subplot(321)
plt.plot(data)
t=np.arange(0,(len(data)/np.float(fs)),1.0/fs)
plt.subplot(322)
plt.plot(t,data)


fs,data=wav.read('jas22.wav')
print (fs, len(data),data)
plt.subplot(323)
plt.plot(data)
t=np.arange(0,(len(data)/np.float(fs)),1.0/fs)
plt.subplot(324)
plt.plot(t,data)


wav.write('audio.wav',fs*2,data)
fs1,data1=wav.read('audio.wav')
print (fs1, len(data1),data1)
plt.subplot(325)
plt.plot(data1)
t=np.arange(0,(len(data1)/np.float(fs1)),1.0/fs1)
plt.subplot(326)
plt.plot(t,data1)
plt.show()
