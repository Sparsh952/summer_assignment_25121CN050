#1  Write a program to Add matrices


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []
result = []

print("Enter elements of first matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input())
        row.append(num)
    matrix1.append(row)

print("Enter elements of second matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input())
        row.append(num)
    matrix2.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Sum of the matrices:")
for row in result:
    print(row)




#2  Write a program to Subtract matrices.    


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []
result = []

print("Enter elements of first matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input())
        row.append(num)
    matrix1.append(row)

print("Enter elements of second matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input())
        row.append(num)
    matrix2.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)

print("Difference of the matrices:")
for row in result:
    print(row)




#3  Write a program to Transpose matrix.


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input())
        row.append(num)
    matrix.append(row)

transpose = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose of the matrix:")
for row in transpose:
    print(row)    




#4  Write a program to Find diagonal sum


n = int(input("Enter the size of the square matrix: "))

matrix = []

print("Enter the elements of the matrix:")
for i in range(n):
    row = []
    for j in range(n):
        num = int(input())
        row.append(num)
    matrix.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum = diagonal_sum + matrix[i][i]

print("Sum of the main diagonal elements =", diagonal_sum)    


