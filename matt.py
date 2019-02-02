
import numpy as np
m=int(input("Enter no. of rows:"))
n=input(("Enter no. of clmns:"))
print("Enter elements:")
a=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		a[i][j]=input(" ")
p=int(input("Enter no. of rows:"))
q=input(("Enter no. of clmns:"))
print("Enter elements:")
b=np.zeros((p,q))
for i in range(p):
	for j in range(q):
		b[i][j]=input(" ")
r=np.zeros((m,q))
if (n==p):
	print ("Multiplication of two matrices")
	
	for i in range(m):
		for k in range(q):
			sum=0
			for j in range(n):
				sum=sum+a[i][j]*b[j][k]
			r[i][k]=sum
	
	print r
else:
	print("Matrix Multiplication is not possible")
		
		