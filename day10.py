#1  Write a program to Print star pyramid.
#        *
#       ***
#      *****
#     *******
#    *********


n=5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))




# #2  Write a program to Print reverse pyramid.
# ********* 
#  *******
#   *****
#    ***
#     * 

n = 5

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))




#3  Write a program to Print number pyramid.
#  1
#  121
#  12321
# 1234321
# 123454321


n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()




#4  Write a program to Print character pyramid. 
#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA    


n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i):
        print(chr(65 + j), end="")

    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()