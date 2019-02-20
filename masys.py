import numpy as np
import matplotlib.pyplot as plt
def movavg(x):
	p=int(input("Enter Order"))
	n=len(x)
	z=[ ]
	for i in range(n):
		sum=0
		for k in range(p):
			if i-k<n and i-k>=0:
				sum=sum+x[i-k]
		y=float(sum)/float(p)
		z=np.append(z,y)
	return (z)

x=[ ]
g=int(input("Enter no. of samples:"))
for j in range(g):
	s=int(input("Enter:"))
	x=np.append(x,s)
print (x)
	
result=movavg(x)
print (result)

f1=int(input("enter signal1 frequency:"))
fs=int(input("enter samplingfrequency:"))
x1=np.arange(0,100,0.1)
y1=np.sin(2*np.pi*(float(f1)/float(fs))*x1)
plt.subplot(221)
plt.plot(y1)
N=np.random.rand(y1.shape[0])
plt.subplot(222)
plt.plot(N)
y2=y1+N
plt.subplot(223)
plt.plot(y2)
d=movavg(y2)
plt.subplot(224)
plt.plot(d)
plt.ylabel('Amplitude')
plt.xlabel('Samples')
plt.show()

#INPUTS:
#enter signal1 frequency:20
#enter samplingfrequency:500 
#Enter Order100
