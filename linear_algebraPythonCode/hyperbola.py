# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import warnings
import math as m
warnings.filterwarnings("ignore")
fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111, aspect='equal')
len = 2000
y= np.linspace(-10,10,len)

#Hyperbola parameters
# given equation values x^TVx+2u^Tx+f=0
V1 = np.array(([8,5],[5,-3]))
u1 = np.array(([-1,2]))
f1 = -2

#Reflection matrix
R1 = np.array(([0,1],[1,0]))
#Eigenvalues and eigenvectors
D_vec1,P1 = LA.eig(V1) 
D1= np.diag(D_vec1)
#Generating the positive hyperbola at the origin
x1 = np.sqrt((1-D_vec1[1]*(y**2))/D_vec1[0])
#Affine transformation parameters
c1 = -LA.inv(V1)@u1 #c=-V^(-1)u
k1 = np.sqrt(np.abs(f1 +u1@c1 ))
print("centre",c1)
#Affine transform 
z1 = np.hstack((np.vstack((x1,y)),np.vstack((-x1,y))))
x_vec1 = k1*P1.T@R1@z1+c1[:,None]

#centre and modified centre 
xc=[-1/7]
yc=[3/7]

# plotting given hyperbola 

plt.plot(x_vec1[0,0:len],x_vec1[1,0:len], color='b')
plt.plot(x_vec1[0,len:2*len],x_vec1[1,len:2*len], color='b', label = '$8x^2+10xy-3y^2-2x+4y-2=0$')
plt.plot(xc[0],yc[0],marker='o',color='black',label='centre (-1/7,3/7)') # origin point 
# x-y axis with origin (0,0)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.xlabel('$x-axis$');plt.ylabel('$y-axis$')

plt.xlim([-10, 10])
plt.ylim([-10,10])

#annotate centre points 
for x,y in zip(xc, yc):
    label = '  c ( %d, %d )' % (x, y)
    ax.text(x, y, label,color='r')

plt.legend(bbox_to_anchor=(0.8, 1), loc='lower center')
plt.grid()

plt.show()
