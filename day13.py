#1  # Input and display array

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array elements are:")
for i in arr:
    print(i, end=" ")




#2  Write a program to Find sum and average of array


n = int(input("Enter the number of elements: "))

arr = []
total = 0

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    total = total + num

average = total / n

print("Sum =", total)
print("Average =", average)




#3  Write a program to Find largest and smallest elements


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element =", largest)
print("Smallest element =", smallest)




#4  Write a program to Count even and odd elements


n = int(input("Enter the number of elements: "))

arr = []
even = 0
odd = 0

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even elements =", even)
print("Number of odd elements =", odd)