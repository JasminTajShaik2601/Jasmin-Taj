import numpy as np
import matplotlib.pyplot as plt

f1=input("Enter input signal frequency f1:")
f2=input("Enter input signal frequency f2:")
fs=input("Enter sampling frequency:")
x1=np.arange(0,10,0.1)
y1=np.cos((2*np.pi*x1*(float(f1)/float(fs))))
x2=np.arange(0,10,0.1)
y2=np.sin((2*np.pi*x2*(float(f2)/float(fs))))
x3=x1+x2
y3=y1+y2

plt.subplot(3,1,1)
plt.plot(x1,y1)

plt.subplot(3,1,2)
plt.plot(x2,y2)
plt.subplot(3,1,3)
plt.plot(x3,y3)

plt.xlabel('samples')
plt.ylabel('voltage')
plt.show( )

