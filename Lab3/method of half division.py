def f(x):
   f1 = 12*x**3 -12*x**2 +4*x - 4
   return f1
def function(a, b, e):
    while (abs(b-a) > e):
      c = (a+b) / 2.0
      if (f(a) - f(c) < 0):
         b = c
      else:
         a = c
    x = (a + b) / 2
    print (x)
    return x
function (-0.5, 1, 0.0001)