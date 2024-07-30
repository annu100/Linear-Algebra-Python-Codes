import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2, 2, 40)
y = np.linspace(-3, 3, 400)
x, y = np.meshgrid(x, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
axes()
plt.contour(x, y, 8*x*x+10*x*y-3*y*y-2*x+4*y-2, [0], colors='k', legend= 'adfdsffdsf')
plt.contour(x, y, 8*x*x+10*x*y-3*y*y-2*x+4*y, [0], colors='r')
plt.contour(x, y, 8*x*x+10*x*y-3*y*y-2*x+4*y-1, [0], colors='g')
plt.plot(a, 0, '.')
plt.axvline(-a)
plt.show()
