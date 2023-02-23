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


def multiply_matrices(matrix1, matrix2):
    result_matrix = [[0 for j in range(len(matrix2[0]))]
                     for i in range((len(matrix1)))]
    # create a matrix j passes on the cols of the 2nd matrix and i on 1st one rows
    for row in range(len(matrix1)):
        for col in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[row][col] += matrix1[row][k] * matrix2[k][col]
    return result_matrix


if c1 == r2:
    # initialize the matrix of zero values
    mat1 = [[random.randint(1, 20) for j in range(c1)] for i in range(r1)]
    mat2 = [[random.randint(1, 20) for j in range(c2)] for i in range(r2)]
    ansMat = [[0 for j in range(c2)] for i in range(r1)]
    '''
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
    '''
    print_matrix(mat1)

    print("*******************************************")  # print
    '''
    # for i in range(r2):
    #     for j in range(c2):
    #         print(mat2[i][j], end=' ')
    #     print()  # add a newline after each row
    '''
    print_matrix(mat2)

    print("============================================")  # print
    '''
    # for i in range(r1):
    #     for j in range(c2):
    #         for k in range(r2):
    #             ansMat[i][j] += mat1[i][k] * mat2[k][j]
    '''
    ansMat = multiply_matrices(mat1, mat2)

    print_matrix(ansMat)

else:  # c1 should = r2
    print("First matrix must have the same number of columns as the second matrix has rows c1 should = r2 ")
