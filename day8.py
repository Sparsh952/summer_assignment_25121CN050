#1 Write a program to Print half pyramid pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


#2  Write a program to Print number triangle.
# 1
# 12
# 123
# 1234
# 12345


rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


#3  Write a program to Print character triangle.
# A
# AB
# ABC
# ABCD
# ABCDE

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


#4  Write a program to Print repeated-number pattern
# 1
# 22
# 333
# 4444
# 55555

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end="")
    print()

    