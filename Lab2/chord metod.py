def f(x):
   return 6 * x**4 + 4 * x**3 - x**2  - x - 10
def f_1(x):
     return 72 * x**2 + 24*x - 2
def horda(a, b, e):
    if f(a) * f_1(a)>0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
       
    xi1 = xi- (xi - x0) * f(xi)/ (f(xi) - f(x0))
    
    while abs (xi1 - xi) >= e:
       xi = xi1
       xi1= xi - f(xi) * (xi - x0)/ (f(xi) - f(x0))
    xk = xi1  
    return print(xi)
horda(0.5, 1, 0.01)  
horda(-1, -0.29, 0.01)