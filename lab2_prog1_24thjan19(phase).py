import numpy as np
import matplotlib.pyplot as plt

f1=input("Enter input signal frequency f1:")
f2=input("Enter input signal frequency f2:")
fs=input("Enter sampling frequency:")
x1=np.arange(0,10,0.1)
y1=np.sin((2*np.pi*x1*(float(f1)/float(fs)))+0)
x2=np.arange(0,10,0.1)
y2=np.sin((2*np.pi*x2*(float(f2)/float(fs)))+180)

plt.subplot(2,1,1)
plt.plot(x1,y1)

plt.subplot(2,1,2)
plt.plot(x2,y2)


plt.xlabel('samples')
plt.ylabel('voltage')
plt.show( )

