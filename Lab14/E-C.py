import numpy as np
from matplotlib import pyplot as plt
x0 = 1.7
y0 = 5.3
xp = 2.7
n = 11
h = (xp-x0)/(n-1)
print (h)
x = np.linspace(x0,xp,n)
y = np.zeros([n])
y[0] = y0
for i in range(1,n):
    y[i]= y[i-1]+h/(x[i-1]+np.sin(y[i-1]/np.pi)+ x[i+1]+np.sin(y[i-1]+0,1*x[i-1]+ np.sin(y[i-1]/np.pi))/2)
for i in range (n):
    print('xi = ',round(x[i],1),'      yi =' ,round(y[i],4))
