import matplotlib.pyplot as plt
from numpy import *
from math import *
import sympy as sp
def t(x):
    y = 0
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    print ('1 pohidna = ',d1, '\n2 pohidna = ',d2, '\n3 pohidna = ',d3) 
    y += f + d1*x +d2*(x-0)**2/2 + d3*(x-0)**3/6
    print ('\ny = ',y)
    return y

x = sp.symbols('x') 
f = sp.sin(x)*x**2 
T = t(x)
pl = sp.plot(f, T, (x, -1, 1), label ='Taylor', title = 'Taylor')
pl.show()