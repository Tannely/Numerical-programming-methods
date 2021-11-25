from scipy import integrate
from numpy import *
def f(x):
    return 1/sqrt(x+3)
v,err = integrate.quad(f, 0.4, 1.2) # перевірка для методу прямокутників
def l(f,a,b,n):
  h=(b-a)/n
  sum=0
  for i in range(0,n):
    sum+=f(a+i*h)
  return sum*h
print("Left rectangle = ",l(f,0.4,1.2,10))
 
def r(f,a,b,n):
  h=(b-a)/n
  sum=0
  for i in range(1,1+n):
    sum+=f(a+i*h)
  return sum*h
print("right rectangle = ",r(f,0.4,1.2,10))
 
def s(f,a,b,n):
  h=(b-a)/n
  sum=0
  for i in range(0,n):
    sum+=f(a+i*h/2)
  return sum*h
print("Seredni rectangle = ",s(f,0.4,1.2,10))
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
print ('Check for trapezoidal method = ',v)
def f2(x):
    return (2*x+0.5)*sin(x)
def simpson(f2,a,b,n):
    h = (b - a) / n
    simp = f2(a) + f2(b)
    for i in range(1,n):
        f = a + i*h
        if i%2 == 0:
         simp = simp + 2 * f2(f)
        else:
         simp = simp + 4 * f2(f)   
    simp = simp * h/3
    return simp
print("\nSimpsons method = ",simpson(f2,0.4,1.2,8))
v,err = integrate.quad(f2,0.4, 1.2)#перевірка для методу Сімпсона
print ('Check for Simpsons method = ',v)