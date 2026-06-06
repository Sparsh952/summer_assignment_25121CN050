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





# #2  Write a program to Convert binary to decimal.

# def binary_to_decimal(binary_str):
#     decimal_val = 0
#     power = 0
    
    
#     for digit in reversed(binary_str):
#         if digit == '1':
#             decimal_val += 2 ** power
#         elif digit != '0':
#             return "Invalid binary digit detected!"
#         power += 1
        
#     return decimal_val


