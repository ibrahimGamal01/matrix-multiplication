import numpy as np  # I want to check my solution with numpy
import random
r1 = int(input("Enter matrix 1 number of rows : "))
c1 = int(input("Enter matrix 1 number of cols : "))
r2 = int(input("Enter matrix 2 number of rows : "))
c2 = int(input("Enter matrix 2 number of cols : "))


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


if c1 == r2:
    # initialize the matrix of zero values
    mat1 = [[random.randint(1, 20) for j in range(c1)] for i in range(r1)]
    mat2 = [[random.randint(1, 20) for j in range(c2)] for i in range(r2)]
    ansMat = [[0 for j in range(c2)] for i in range(r1)]

    # Random Values Insertion
    # # isert random values in matrix 1
    # for i in range(r1):
    #     for j in range(c1):
    #         mat1[i][j] = i + j + random.randint(3, 19)

    # # insert random values in matrix 2
    # for i in range(r2):
    #     for j in range(c2):
    #         mat2[i][j] = i + j + random.randint(3, 9)

    # print matr

    print_matrix(mat1)

    print("*******************************************")  # print

    # for i in range(r2):
    #     for j in range(c2):
    #         print(mat2[i][j], end=' ')
    #     print()  # add a newline after each row
    
    print_matrix(mat2)

    print("============================================")  # print

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                ansMat[i][j] += mat1[i][k] * mat2[k][j]

    print_matrix(ansMat)

else:  # c1 should = r2
    print("First matrix must have the same number of columns as the second matrix has rows c1 should = r2 ")
