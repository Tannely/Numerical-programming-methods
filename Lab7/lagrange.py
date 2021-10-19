from numpy import *
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
x= array([-2,0,1,2], dtype=float)
y= array([30,-4,3,18], dtype=float)
def Lagrange(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1   
            else: 
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z =z +y[j]*p1/p2
    return z
xnew = linspace(min(x),max(x))
ynew=[Lagrange(x,y,i) for i in xnew]
plt.plot(x,y,'ro',xnew,ynew, 'b')
plt.grid(color = 'k', 
         linestyle = '-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial')
plt.show()



f = lagrange(x, y)
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial')
plt.grid(color = 'k', 
         linestyle = '-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
        