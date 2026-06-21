#1  Write a program to Find string length without strlen()


text = input("Enter a string: ")

count = 0

for ch in text:
    count = count + 1

print("Length of the string is:", count)




#2  Write a program to Reverse a string


text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string is:", reverse)




#3  Write a program to Count vowels and consonants


text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)




#4  Write a program to Convert lowercase to uppercase


text = input("Enter a string: ")

uppercase_text = text.upper()

print("Uppercase string:", uppercase_text)

