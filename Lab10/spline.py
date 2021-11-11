import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [0.8,1.0,1.3,1.9,2.3]
y = [1.72,2.35,1.52,2.43,1.55]
spl = UnivariateSpline(x, y)
xs = linspace(-2, 5, 1000)
plt.plot(x,y, 'ro', xs, spl(xs), 'g')
plt.grid(color = 'k', 
         linestyle = '-')
plt.xlabel('axis x')
plt.ylabel('axis y')
plt.title('Spline interpolation')  
plt.legend(['x,y - red marker',
            'spl - green marker'],
          loc = 'upper right')     
plt.show()
