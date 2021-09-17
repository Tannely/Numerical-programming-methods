def func(x):
   return 3*x**4 -4*x**3 -4*x - 1
def f1(x):
   return 12*x**3 -12*x**2 +4*x - 4
def f2(x):
    return 36*x**2 - 24*x + 4
def metod(a, b, eps):
    if func(b) * f2(b) > 0:
        x = b
        print("x = b")
    else:
        x = a
   
    h = func(x) / f1(x)
    x = x - h
    if abs(h) <= eps:
      print(x)
    else:
        h = func(x) / f1(x)
        x = x - h
    print('метод Ньютона' '\n', x)   
metod (-0.5, 1, 0.0001) 