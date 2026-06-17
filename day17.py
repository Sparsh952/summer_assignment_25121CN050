#1  Write a program to Merge arrays.


arr1 = list(map(int, input("Enter elements of first array: ").split()))

arr2 = list(map(int, input("Enter elements of second array: ").split()))

merged_array = arr1 + arr2

print("Merged array:", merged_array)




#2  Write a program to Union of arrays.


arr1 = list(map(int, input("Enter elements of first array: ").split()))

arr2 = list(map(int, input("Enter elements of second array: ").split()))

union_array = list(set(arr1 + arr2))

print("Union of arrays:", union_array)




#3  Write a program to Intersection of arrays


arr1 = list(map(int, input("Enter elements of first array: ").split()))

arr2 = list(map(int, input("Enter elements of second array: ").split()))

intersection = list(set(arr1) & set(arr2))

print("Intersection of arrays:", intersection)




#4  Write a program to Find common elements.


arr1 = list(map(int, input("Enter elements of first array: ").split()))

arr2 = list(map(int, input("Enter elements of second array: ").split()))

common = []

for i in arr1:
    if i in arr2 and i not in common:
        common.append(i)


print("Common elements:", common)