import math
import numpy as np
print('Method of Gauss')
a = np.matrix([[3, -5, 3], [1, 2, 1], [2, 7, -1]])
a1 = np.matrix([[1], [4], [8]])
b =  np.linalg.inv(a)
result = b * a1
print(result)
print('\nRevision')
print(np.linalg.solve(a, a1))

"""
a = np.matrix([[3, -5, 3], [1, 2, 1], [2, 7, -1]])
a1 = np.matrix([[1], [4], [8]])
A = np.linalg.solve(a, a1)
print(A) 

"""



