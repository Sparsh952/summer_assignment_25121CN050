#1  Write a program to Convert decimal to binary.

def decimal_to_binary(n):
    if n == 0:
        return "0"
        
    binary_str = ""
    while n > 0:
        remainder = n % 2          
        binary_str = str(remainder) + binary_str  
        n = n // 2                
    return binary_str





#2  Write a program to Convert binary to decimal.

def binary_to_decimal(binary_str):
    decimal_val = 0
    power = 0
    
    
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_val += 2 ** power
        elif digit != '0':
            return "Invalid binary digit detected!"
        power += 1
        
    return decimal_val




#3  Write a program to Count set bits in a number. 


def count_set_bits_loop(n):
    count = 0
    while n > 0:
        
        count += n & 1
        
        n >>= 1
    return count



#4  def power_iterative(x, n):
    
    if n == 0:
        return 1
        
    result = 1.0
    abs_n = abs(n)  
    
    while abs_n > 0:
        result *= x
        abs_n -= 1
        
   
    return 1








