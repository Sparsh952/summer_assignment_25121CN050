#1  Write a program to Linear search.


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter number to search: "))

found = False

for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if found == False:
    print("Element not found")




#2  Write a program to Frequency of an element    


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter the element to find frequency: "))

count = 0

for i in arr:
    if i == key:
        count += 1

print("Frequency of", key, "is", count)




#3  Write a program to Second largest element


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]
second = arr[0]

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest element is:", second)




#4  Write a program to Find duplicates in array. 


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Duplicate elements are:")

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(arr[i])
            break