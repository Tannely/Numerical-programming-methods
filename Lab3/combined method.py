def func(x):
   return 3*x**4 -4*x**3 -4*x - 1
def f1(x):
   return 12*x**3 -12*x**2 +4*x - 4
def f2(x):
    return 36*x**2 - 24*x + 4
def combine(a, b, eps):
    if f1(a) * f2(a) < 0:
        a0 = b
        b0 = a
    else:
        a0 = b
        b0 = a

    xp1 = a0
    xp2 = b0

    xn1 = xp1 - func(xp1) *(xp2 - xp1)/ (func(xp2) - func(xp1))
    xn2 = xp2 - func(xp2)/ f1(xp2)
    xp1 = xn1
    xp2 = xn2

    if xp2 - xp1 < eps:
        x = (xp1 + xp2) / 2
        
    else:
        xn1 = xp1 - func(xp1) *(xp2 - xp1)/ (func(xp2) - func(xp1))
        xn2 = xp2 - func(xp2)/ f1(xp2)
        xp1 = xn1
        xp2 = xn2
    print('Combined method =', x)   
combine (-0.5, 1, 0.0001)         
       
       

 