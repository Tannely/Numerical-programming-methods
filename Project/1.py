from random import randint
import numpy as np
N = 4
M = 5
A = [[0] * M for i in range (N)]
print('Матриця розмірністю 4x5 заповнена випадковими числами в діапазоні від 3 до 23') 
for i in range (N):
    for j in range (M):
        A[i][j] = randint(3, 23)
        print(A[i][j], end = ' ')   
    print()
# sum
print('\n-------------------------Sum-------------------------')   
sum = 0
for i in range (N):
    for j in range (M):
        sum += A[i][j]
print('\nСума елементів матриці =',sum)
sum1 = 0
for i in range(N):
     sum1 += A[i][i]
print('\nСума головної діагоналі матриці =',sum1)      
sum2 = 0
for i in range(0, N):
    for j in range(i+1, M):
        sum2 += A[i][j]
print('\nСума елементів над головною діагоналлю матриці =',sum2)
sum3 = 0
for i in range(1, N):
    for j in range(i):
        sum3 += A[i][j]
print('\nСума елементів під головною діагоналлю матриці =',sum3)

# min, max, indices
print()
print('\n-------------------------Min, Max, Indices-------------------------')
min = A[0][0]
min_i = 0
min_j = 0
for i in range (N):
    for j in range (M):
        if A[i][j] < min:
            min = A[i][j]
            min_i = i
            min_j = j
max = A[0][0]
max_i = 0
max_j = 0   
for i in range (N):
    for j in range (M):  
        if  A[i][j] > max:
            max = A[i][j]
            max_i = i
            max_j = j  
print('\nМінімальний елемент матриці = ', min)
print('Індекс мінімального значення = [{}, {}]'.format(min_i, min_j))
print('\nМаксимальний елемент матриці = ', max)
print('Індекс максимального значення = [{}, {}]'.format(max_i, max_j))
