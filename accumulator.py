import numpy as np
m=int(input("Enter no. of samples:"))
x=[ ]
for i in range (m):
	y=int(input("Enter:"))
	x=np.append(x,y)
print ("Entered Samples",x)
y=[ ]
s=0
for i in range(m):
	s=s+x[i]
	y=np.append(y,s)

print ("Accumulator Result",y)
	
