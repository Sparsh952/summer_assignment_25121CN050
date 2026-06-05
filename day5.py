#1  Write a program to Check perfect number


def is_perfect_number(num):
  
    if num <= 0:
        return False
        
    divisor_sum = 0
    
   
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
            
  
    return divisor_sum == num


user_num = int(input("Enter a number: "))

if is_perfect_number(user_num):
    print(f"{user_num} is a Perfect Number.")

else:
    print(f"{user_num} is not a Perfect Number.")



#2  Write a program to Check strong number.


def is_perfect_number(num):
    if num <= 0:
        return False
    
    divisor_sum = 0
     
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
              
    return divisor_sum == num

user_input = int(input("Enter a positive integer: "))

if is_perfect_number(user_input):
    print(f"{user_input} is a perfect number.")

else:
    print(f"{user_input} is not a perfect number.")


#3  Write a program to Print factors of a number    



def is_perfect_number(num):
    if num <= 0:
        return False
    
    divisor_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
            
    return divisor_sum == num

user_input = int(input("Enter a positive integer: "))

if is_perfect_number(user_input):
    print(f"{user_input} is a perfect number.")

else:
    print(f"{user_input} is not a perfect number.")



#4  Write a program to Print Armstrong numbers in a range


lower = int(input("Enter lower bound of the range: "))
upper = int(input("Enter upper bound of the range: "))

print(f"Armstrong numbers between {lower} and {upper} are:")


for num in range(lower, upper + 1):
    order = len(str(num))
    temp = num
    digit_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += digit ** order
        temp //= 10
    if num == digit_sum:
        print(num, end=" ")


