import numpy as np
a = np.random.randint(10,50 , size=(5,5))
print('Матриця розмірністю 5x5 заповнена випадковими числами від 10 до 50\n',a)
# types of matrices
print()
print('\n-------------------------Types of matrices-------------------------')
print()
print('\nОбернена матриця\n', np.linalg.inv(a))
print('\nТранспортована матриця\n', a.T)

# actions on matrices
print()
print('\n-------------------------Actions on matrices-------------------------')
print()
print('\nПіднесення до 2 степеня \n', np.linalg.matrix_power(a, 2))
print('\nВизначник матриці =', round(np.linalg.det(a), 3))
print('\nРанг матриці =', np.linalg.matrix_rank(a))

# sum
print()
print('\n-------------------------Sum-------------------------')
print()
print('\nСума всіх елементів матриці =', np.sum(a))
print('\nСума кожного з рядків матриці =', np.sum(a, axis = 1))
print('\nСума кожного із стовців матриці =', np.sum(a, axis = 0))


#average values
print()
print('\n-------------------------Average values-------------------------')
print()
print('\nCередні значення рядків = ', np.mean(a, axis = 1))
print('\nCередні значення cтовпців = ', np.mean(a, axis = 0))

#diagonal elements and sum
print()
print('\n-------------------------Diagonal elements and sum-------------------------')
print()
print('\nЕлементи головної діагоналі матриці =', np.diagonal(np.asarray(a)))
print('\nСума елементів головної діагоналі матриці =', np.trace(np.asarray(a)))
b = np.asarray(a)
b = np.fliplr(b)
print('\nЕлементи побічної діагоналі матриці =', np.diagonal(b))
print('\nСума елементів побічної діагоналі матриці =', np.trace(b))

# min, max, indices
print()
print('\n-------------------------Min, Max, Indices-------------------------')
print()
print('\nМінімальний елемент матриці =', np.amin(a))
print('\nІндекс мінімального значення матриці =', np.unravel_index(np.argmin(a), a.shape))
print('\nІндекс максимального значення матриці =', np.unravel_index(np.argmax(a), a.shape))
print('\nМаксимальний елемент матриці =', np.amax(a))
print('\nІндекси мінімальних значень рядків матриці =', np.argmin(a, axis = 1))
print('\nІндекси максимальних значень стовпців матриці =', np.argmax(a, axis = 0))
print('\nМінімальні елементи рядків матриці =', np.amin(a, axis = 1))
print('\nМаксимальні елементи стовпців матриці =', np.amax(a, axis = 0))