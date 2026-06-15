#1  Write a program to Reverse array.


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

arr.reverse()

print("Reversed array:")
for i in arr:
    print(i, end=" ")



#2  Write a program to Rotate array left.


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

first = arr[0]

for i in range(n - 1):
    arr[i] = arr[i + 1]

arr[n - 1] = first

print("Array after left rotation:")
for i in arr:
    print(i, end=" ")




#3  Write a program to Rotate array right


# Input array elements
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Right rotation
last = arr[n - 1]

for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last

# Display rotated array
print("Array after right rotation:")
for i in arr:
    print(i, end=" ")




#4  Write a program to Move zeroes to end.


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

result = []

for i in arr:
    if i != 0:
        result.append(i)


zero_count = arr.count(0)

for i in range(zero_count):
    result.append(0)


print("Array after moving zeroes to end:")
for i in result:
    print(i, end=" ")