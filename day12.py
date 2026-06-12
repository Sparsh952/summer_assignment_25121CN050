#1  Write a program to Write function for palindrome


def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

value = input("Enter a word or number: ")

if palindrome(value):
    print("Palindrome")
else:
    print("Not a Palindrome")




#2  Write a program to Write function for armstrong 


def armstrong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    if total == num:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

    


#3 Write a program to Write function for fibonnaci
 
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter the number of terms: "))
fibonacci(n)    




#4  Write a program to Write function for perfect number


def perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if perfect(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")