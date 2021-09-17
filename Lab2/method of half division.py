def f(x):
   return 24*x**3 + 1*x**2 -2*x - 1
  
def function(a, b, e):
    while abs(b-a) > e:
      c = (a+b) / 2.0
      if (f(a) - f(c) < 0):
         b = c
      else:
         a = c
    x = (a + b) / 2 
    print (x)
    return x
function (0.5, 1, 0.0001)  