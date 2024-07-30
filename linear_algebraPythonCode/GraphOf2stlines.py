import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5,100)
y_1 = (4*x+1) # straight line 1
y_2 = (1-2*x)/3 # straighe line 2
plt.plot(x, y_2, '-r', label='2x+3y-1=0')
#plt.title('Graph of 2*x-3*y+1')
plt.plot(x, y_1, '-b', label='4x-y+1')
plt.title('Graph of two straight lines')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='best')
plt.grid()
plt.show()
