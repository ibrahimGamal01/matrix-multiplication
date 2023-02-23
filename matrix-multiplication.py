import numpy as np  # I want to check my solution with numpy
import random
r1 = int(input("Enter matrix 1 number of rows : "))
c1 = int(input("Enter matrix 1 number of cols : "))
r2 = int(input("Enter matrix 2 number of rows : "))
c2 = int(input("Enter matrix 2 number of cols : "))

# initialize the matrix of zero values
mat1 = [[0 for j in range(c1)] for i in range(r1)]
mat2 = [[0 for j in range(c2)] for i in range(r2)]
ansMat = [[0 for j in range(c2)] for i in range(r2)]

# Random Values Insertion
# isert random values in matrix 1
for i in range(r1):
    for j in range(c1):
        mat1[i][j] = i + j + random.randint(3, 19)

# insert random values in matrix 2
for i in range(r2):
    for j in range(c2):
        mat2[i][j] = i + j + random.randint(3, 9)

# print matr

for i in range(r1):
    for j in range(c1):
        print(mat1[i][j], end=' ')
    print()  # add a newline after each row

print("*******************************************")  # print

for i in range(r2):
    for j in range(c2):
        print(mat2[i][j], end=' ')
    print()  # add a newline after each row

print("============================================")  # print

for i in range(r1):
    for j in range(c2):
        for k in range(r2):
            ansMat[i][j] += mat1[i][k] * mat2[k][j]

for i in range(r1):
    for j in range(c2):
        print(ansMat[i][j], end=' ')
    print()
