#1 Write a program to Check whether a number is prime

import math

def is_prime(num):
    
    if num <= 1:
        return False
    
    
    if num == 2:
        return True
    
   
    if num % 2 == 0:
        return False
   
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False 
            
    return True 


try:
    user_num = int(input("Enter an integer to check: "))
    if is_prime(user_num):
        print(f"{user_num} is a prime number.")
    else:
        print(f"{user_num} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")



#2 Write a program to Print prime numbers in a range

    
lower_value = int(input("Enter the lower bound of the range: "))
upper_value = int(input("Enter the upper bound of the range: "))

print(f"Prime numbers between {lower_value} and {upper_value} are:")


for num in range(lower_value, upper_value + 1):
    
    if num > 1:
       
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break  
        else:
           
            print(num, end=" ")



#3 Write a program to Find GCD of two numbers


import math


num1 = 60
num2 = 48


result = math.gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")


#4 Write a program to Find LCM of two numbers.


import math


num1 = 12
num2 = 14


result = math.lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {result}")









