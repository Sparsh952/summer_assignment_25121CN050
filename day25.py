#1  Write a program to Merge two sorted arrays


n1 = int(input("Enter number of elements in first sorted array: "))
arr1 = []

print("Enter elements of first sorted array:")
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Enter number of elements in second sorted array: "))
arr2 = []

print("Enter elements of second sorted array:")
for i in range(n2):
    arr2.append(int(input()))

merged = []
i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("Merged sorted array:", merged)




#2  Write a program to Find common characters in string


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Common characters are:")

for ch in str1:
    if ch in str2:
        print(ch, end=" ")




#3  Write a program to Sort names alphabetically


n = int(input("Enter the number of names: "))

names = []

for i in range(n):
    name = input("Enter name: ")
    names.append(name)

names.sort()

print("Names in alphabetical order:")
for name in names:
    print(name)        




#4  Write a program to Sort words by length


sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort(key=len)

print("Words sorted by length:")
for word in words:
    print(word)    