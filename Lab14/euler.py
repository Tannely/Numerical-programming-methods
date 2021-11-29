import numpy as np
from matplotlib import pyplot as plt
x0 = 0.8
y0 = 1.4
xp = 1.8
n = 11
h = (xp-x0)/(n-1)
print (h)
x = np.linspace(x0,xp,n)
y = np.zeros([n])
y[0] = y0
for i in range(1,n):
    y[i]= y[i-1] + h*(x[i-1]+np.cos(y[i-1]/np.sqrt(2)))
for i in range (n):
    print('xi = ',round(x[i],1),'      yi =' ,round(y[i],4))
plt.plot(x,y, 'rs-')
plt.grid(color = 'k', 
         linestyle = '-')
plt.title('Euler’s Method')   
plt.xlabel('x')
plt.ylabel('y')
plt.show()