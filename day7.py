#1  Write a program to Recursive factorial.

def recursive_factorial(n):
    
    if n == 0 or n == 1:
        return 1
 
    else:
        return n * recursive_factorial(n - 1)


num = 5

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {recursive_factorial(num)}")



#2  Write a program to Recursive Fibonacci.


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


n_terms = 10


if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(recur_fibo(i), end=" ")



#3  Write a program to Recursive sum of digits


def sum_of_digits(n):
   
    if n == 0:
        return 0
    
   
    return (n % 10) + sum_of_digits(n // 10)

def get_sum(number):
    
    return sum_of_digits(abs(number))



#4  Write a program to Recursive reverse number.


def reverse_recursive(n, reversed_num=0):
    
    if n == 0:
        return reversed_num
    
    
    new_reversed = (reversed_num * 10) + (n % 10)
    
    
    return reverse_recursive(n // 10, new_reversed)

def reverse_number(number):
    
    sign = -1 if number < 0 else 1
    
    
    return sign * reverse_recursive(abs(number))


