import numpy as np
m=int(input("Enter no. of rows:"))
n=input(("Enter no. of clmns:"))
if (m==n):
	print("Enter elements:")
	a=np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			a[i][j]=input(" ")
	print ("Given Matrix:")
	print a
	y=np.linalg.det(a)
	print("Determinant of given matrix")
	print y
	if(y!=0):
		r=np.linalg.inv(a)
		print("Inverse of given matrix")
		print r
	else:
		print("Matrix inverse is not possible as det is zero")
else:
	print("Given matrix is not suitable to perform matrix inverse")
