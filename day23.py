#1  Write a program to Find first non-repeating character


string = input("Enter a string: ")

for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found.")




#2  Write a program to Find first repeating character


string = input("Enter a string: ")

found = False

for ch in string:
    if string.count(ch) > 1:
        print("First repeating character is:", ch)
        found = True
        break

if found == False:
    print("No repeating character found.")     




#3  Write a program to Check anagram strings. 


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")




#4  Write a program to Find maximum occurring character


string = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in string:
    count = string.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Maximum occurring character is:", max_char)
print("It occurs", max_count, "times.")
