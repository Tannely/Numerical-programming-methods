"""import numpy as np

a = np.random.randint(20, size=(2,2))
print(a)
print(" Element sum in str = " , a.sum(axis=1))
print(" Element sum in str = " , a.sum(axis=0))
rank = np.linalg.matrix_rank(a)
print('Ранг матриці =', rank)
b = np.linalg.det(a)
print (b)"""
rint('\nCереднє значення стовпців')
c = np.mean(A, axis = 0)
print(c)
print('\nCереднє значення рядків')
c1 = np.mean(A, axis = 1)