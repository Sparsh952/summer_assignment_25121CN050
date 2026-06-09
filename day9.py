#1  Write a program to Print reverse star pattern.
# *****
# ****
# ***
# **
# *

rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# #2  Write a program to Print reverse number triangle
# 12345
# 1234
# 123
# 12
# 1

rows = 5

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



#3  Write a program to Print repeated character pattern
# A
# BB
# CCC
# DDDD
# EEEEE

rows = 5

for i in range(1, rows + 1):
    ch = chr(64 + i)   # A, B, C, D, E
    for j in range(i):
        print(ch, end="")
    print()


#4  Write a program to Print hollow square pattern
# *****
# *   *
# *   *
# *   *
# *****


rows = 5

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()