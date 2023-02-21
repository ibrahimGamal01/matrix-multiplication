import random
r1 = int(input("Enter mat1 row size: "))
c1 = int(input("Enter mat1 col size: "))
# r2 = int(input("Enter mat2 row size: "))
# c2 = int(input("Enter mat2 col size: "))

mat1 = [[0 for j in range(c1)] for i in range(r1)]

for i in range(r1):
    for j in range(c1):
        mat1[i][j] = i+ j + random.randint(3,9)

for i in range(r1):
    for j in range(c1):
        print(mat1[i][j], end=' ')
    print()  # add a newline after each row
