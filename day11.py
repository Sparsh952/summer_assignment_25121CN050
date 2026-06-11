#1  Write a program to Write function to find sum of two number

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum =", result)




#2  Write a program to Write function to find maximum

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


result = maximum(num1, num2)


print("Maximum number =", result)




#3  Write a program to Write function to check prime


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))


if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")




#4  Write a program to Write function to find factorial


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number: "))


result = factorial(num)


print("Factorial =", result)
