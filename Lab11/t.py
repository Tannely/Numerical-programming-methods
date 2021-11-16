import matplotlib.pyplot as plt
from numpy import *
import math
t = linspace(-1, 1)
y1 = t**2*sin(t)
y2 = y1+(t**2*cos(t)+ 2*t*sin(t))*t +(-t**2*sin(t) + 4*t*cos(t) + 2*sin(t))*(t-0)**2/2+(-t**2*cos(t) - 6*t*sin(t) + 6*cos(t))*(t-0)**3/6
plt.grid(color = 'k', 
         linestyle = '-')
plt.plot(t, y1, 'g-', t, y2, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor')
plt.legend(['x^2sin(x)',
            'approximation'],
           loc = 'upper right')
plt.show()