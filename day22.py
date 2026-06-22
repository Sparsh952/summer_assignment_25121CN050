#1  Write a program to Check palindrome string.


text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")




#2  Write a program to Count words in a sentence


sentence = input("Enter a sentence: ")

words = sentence.split()

count = len(words)

print("Number of words:", count)




#3  Write a program to Character frequency.


text = input("Enter a string: ")

for ch in text:
    count = text.count(ch)
    print(ch, ":", count)




#4  Write a program to Remove spaces from string


text = input("Enter a string: ")

result = text.replace(" ", "")

print("String without spaces:", result)    
