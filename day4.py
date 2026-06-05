#1  Write a program to Generate Fibonacci series.



nterms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1


#2  Write a program to Find nth Fibonacci term.


n = int(input("Enter the value of n: "))

a, b = 0, 1

if n == 1:
    print("Fibonacci term:", a)
elif n == 2:
    print("Fibonacci term:", b)
else:
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print("Fibonacci term:", b)


#3  Write a program to Check Armstrong number.

num = int(input("Enter a number: "))

temp = num
order = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


#4   Write a program to Print Armstrong numbers in a range 

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    order = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    if total == num:
        print(num)



