#1  Write a program to Find missing number in array


n = int(input("Enter the value of n: "))

arr = list(map(int, input("Enter the array elements: ").split()))

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum

print("Missing number is:", missing_number)




#2  Write a program to Find maximum frequency element


arr = list(map(int, input("Enter array elements: ").split()))

max_freq = 0
max_element = arr[0]

for i in arr:
    freq = arr.count(i)
    
    if freq > max_freq:
        max_freq = freq
        max_element = i

print("Element with maximum frequency:", max_element)
print("Frequency:", max_freq)




#3  Write a program to Find pair with given sum.


arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter the required sum: "))

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], "and", arr[j])
            found = True

if not found:
    print("No pair found")




#4  Write a program to Remove duplicates from array


arr = list(map(int, input("Enter array elements: ").split()))

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print("Array after removing duplicates:")
print(new_arr)

