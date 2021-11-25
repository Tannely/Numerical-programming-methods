from scipy import integrate
from numpy import *
def f(x):
    return 1/sqrt(x+3)
v,err = integrate.quad(f, 0.4, 1.2) # перевірка для методу прямокутників
print ('Check for the ractangle method = ',v)
def f1(x):
    return 1/sqrt(0.5*x**2+1.5)
def tr_int(f1,a,b,n):
    h=(b-a)/n
    sum =0.5 * (f1(a)+ f1(b))
    for i in range(1,n):
        sum += f1(a+i*h)
    return sum*h    
print ('\nTrapezoidal method = ',tr_int(f1,1.2, 2, 20))  
v,err = integrate.quad(f1,1.2, 2)#перевірка для методу трапецій
print ('\nCheck for trapezoidal method = ',v)