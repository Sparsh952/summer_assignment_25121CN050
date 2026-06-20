#1  Write a program to Multiply matrices


rows1 = int(input("Enter rows of first matrix: "))
cols1 = int(input("Enter columns of first matrix: "))

rows2 = int(input("Enter rows of second matrix: "))
cols2 = int(input("Enter columns of second matrix: "))

if cols1 != rows2:
    print("Matrix multiplication is not possible.")
else:
    
    print("Enter elements of first matrix:")
    matrix1 = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = int(input())
            row.append(element)
        matrix1.append(row)

    print("Enter elements of second matrix:")
    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = int(input())
            row.append(element)
        matrix2.append(row)

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            row.append(0)
        result.append(row)

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

    print("Resultant Matrix:")
    for i in range(rows1):
        for j in range(cols2):
            print(result[i][j], end=" ")
        print()




#2  Write a program to Check symmetric matrix


n = int(input("Enter the order of the matrix: "))

matrix = []

print("Enter the elements of the matrix:")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input())
        row.append(element)
    matrix.append(row)

symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("The matrix is Symmetric.")
else:
    print("The matrix is Not Symmetric.")        




#3  Write a program to Find row-wise sum.


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix.append(row)

print("Row-wise Sum:")
for i in range(rows):
    total = 0
    for j in range(cols):
        total = total + matrix[i][j]
    print("Sum of Row", i + 1, "=", total)    




#4  Write a program to Find column-wise sum. 


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix.append(row)

print("Column-wise Sum:")
for j in range(cols):
    total = 0
    for i in range(rows):
        total = total + matrix[i][j]
    print("Sum of Column", j + 1, "=", total)    



