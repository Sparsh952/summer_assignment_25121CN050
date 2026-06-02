#Write a program to Find sum of digits of a number


num = int(input("Enter a number: "))

digit_sum = 0

while num > 0:
    last_digit = num % 10    
    digit_sum += last_digit  
    num = num // 10  

print("The sum of the digits is:", digit_sum)


#Write a program to Reverse a number


num = int(input("Enter a number: "))

reversed_num = 0


while num > 0:
    digit = num % 10                  # Extract the last digit
    reversed_num = (reversed_num * 10) + digit  # Build the reversed number
    num = num // 10                   # Remove the last digit


print("Reversed number:", reversed_num)


#Write a program to Find product of digits. 


num = int(input("Enter a number: "))

product = 1


while num > 0:
    
    digit = num % 10
    
    product = product * digit
    
    num = num // 10


print("The product of the digits is:", product)


#Write a program to Check whether a number is palindrome



num = int(input("Enter a number: "))

product = 1

while num > 0:
    
    digit = num % 10
    
    product = product * digit
    
    num = num // 10

print("The product of the digits is:", product)





