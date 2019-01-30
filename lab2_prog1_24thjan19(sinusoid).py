import numpy as np
import matplotlib.pyplot as plt

f=input("Enter input signal frequency:")
fs=input("Enter sampling frequency:")

x=np.arange(0,10,0.1)
y=np.cos(2*np.pi*x*(float(f)/float(fs)))
plt.plot(x,y)
plt.xlabel('samples')
plt.ylabel('voltage')
plt.show( )