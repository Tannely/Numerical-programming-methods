from scipy import optimize
import math
def f(x):
    return [math.cos(x[0] + 0.5) - x[1] - 2.0, math.sin(x[1]) -2.0*x[0] -1.0]
sol = optimize.root(f, [0, 0], method = 'hybr')    
print (sol.x)