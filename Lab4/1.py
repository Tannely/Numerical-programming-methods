import numpy as np
# завдання 1
print('\n Task 1')
a = ([[1, 2], [4, -1]])
print ('A=', a)
b = np.matrix([[2, -3], [-4, 1]])
print ('B=', b)
print ('Множення матриць A*B =',a*b)
print ('Множення матриць B*A =',b*a)
print ('Множення матриць B*A =',b*a)
print ('Віднімання матриць: AB-BA =',a*b - b*a)

# завдання 2
print('\n Task 2')
с = np.matrix([[-1, 2], [0, 1]])
result = np.linalg.matrix_power(с, 2)
print('Піднесення до 2 степеня =', result)

#  завдання 3
print('\n Task 3')
d = np.matrix([[3, 5], [6, -1]])
d1 = np.matrix([[2, 1], [-3, 2]])
D = d.dot(d1)
print('Множення матриць =', D)

# завдання 4
print('\n Task 4')
e = np.matrix([[2, 3, 4], [1, 0, 6], [7, 8, 9]])
e1 = round(np.linalg.det(e), 3)
print('Визначник1 =', e1)
# Завдання 5
print('\n Task 5')
f = np.matrix([[1, 2, 3, 4], [-2, 1, -4, 3], [3, -4, -1, 2], [4, 3, -2, -1]])
f1 = round(np.linalg.det(f), 3)
print('Визначник2 =', f1)
# завдання 6
print('\n Task 6')
j = np.matrix([[1, 2, -3], [0, 1, 2], [0, 0, 1]])
j_inv = np.linalg.inv(j)
print('Обернена матриця =', j_inv)
# завдання 7
print('\n Task 7')
i = np.matrix([[1, 2, 3, 4], [3, -1, 2, 5], [1, 2, 3, 4], [1, 3, 4, 5]])
rank = np.linalg.matrix_rank(i)
print('Ранг матриці =', rank)
# завдання 8
print('\n Task 8 ')
matrix = np.matrix([[14, 4, 6], [5, -3, 2], [10, -11, 5]])
matrixv1 = np.matrix([[30], [15], [36]])
matrixa1 = np.matrix([[30, 4, 6], [15, -3, 2], [36, -11, 5]])
matrixb1 = np.matrix([[14, 30, 6], [5, 15, 2], [10, 36, 5]])
matrixz1 = np.matrix([[14, 4, 30], [5, -3, 15], [10, -11, 36]])
a2 = np.linalg.det(matrixa1)
b2 = np.linalg.det(matrixb1)
z2 = np.linalg.det(matrixz1)
x8 = np.linalg.det(matrix)
if x8 != 0:
    x = round((a2/ x8), 3)
    y = round((b2/ x8),3)
    z = round((z2/ x8),3)
print("x =" ,x,"y =", y,"z =", z)
print("Revision = ")
print(np.linalg.solve(matrix, matrixv1))
# завдання 9
print(' Task 9 ')
# 5 приклад
n = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
n1 = np.matrix([[-2], [-1], [-0]])
j6 =  np.linalg.inv(n)
result = j6 * n1
print(result)
print("revision = ")
print(np.linalg.solve(n, n1))



