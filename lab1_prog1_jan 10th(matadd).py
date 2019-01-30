import numpy as np
m=int(input("Enter no. of rows:"))
n=input(("Enter no. of clmns:"))
print("Enter elements:")
a=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		a[i][j]=input(" ")
print("Enter elements:")
b=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		b[i][j]=input(" ")
r=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		r[i][j]=a[i][j]+b[i][j]
print ("Addition of two matrices")
print (r)




