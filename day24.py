#1  Write a program to Check string rotation.


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")




#2  Write a program to Compress a string. 


s = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        compressed = compressed + s[i] + str(count)
        count = 1

print("Compressed string:", compressed)    




#3  Write a program to Find longest word. T


sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
print("Length:", len(longest_word))




#4  Write a program to Remove duplicate characters


string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)
