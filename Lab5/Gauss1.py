import numpy as np
def gauss(a, b):
    print('\n Revision \n', np.linalg.solve(a, b))
    print('\n Method of Jordan Gaus \n', np.linalg.inv(a) *b)
    n = len(b)
# Фаза виключення 
    for k in range (1,n):
        for i in range (k+1,n):
            if a[i,k] != 0:
               a[i,k+1:n] = a[i,k+1:n] - a [i,k]/a[k,k] *a[k,k+1:n]
               b[i] = b[i] -a [i,k]/a[k,k] *b[k]
# Зворотний хід
    for k in range (n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
    
    return b
gauss(np.matrix([[3, -5, 3], [1, 2, 1], [2, 7, -1]]), np.matrix([[1], [4], [8]]))  