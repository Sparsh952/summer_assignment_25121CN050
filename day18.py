#1  Write a program to Bubble sort.


n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap the elements
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array is:")
for i in arr:
    print(i, end=" ")




#2  Write a program to Selection sort.


n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print("Sorted array is:")
for i in arr:
    print(i, end=" ")    




#3  Write a program to Binary search.


n = int(input("Enter the number of elements: "))

arr = []

print("Enter the sorted elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

key = int(input("Enter the element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found == False:
    print("Element not found")




#4  Write a program to Sort array in descending order


n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            # Swap elements
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Array in descending order:")
for i in arr:
    print(i, end=" ")
