#1  Write a program to Create number guessing game

import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break




#2  Write a program to Create voting eligibility system


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")    




#3  Write a program to Create ATM simulation 


balance = 10000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit successful.")
    print("New balance is:", balance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful.")
        print("Remaining balance is:", balance)
    else:
        print("Insufficient balance.")

elif choice == 4:
    print("Thank you for using the ATM.")

else:
    print("Invalid choice.")    




#4  Write a program to Create quiz application.


score = 0

print("Welcome to the Quiz!")

# Question 1
answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is New Delhi.")

# Question 2
answer = input("2. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is 7.")

# Question 3
answer = input("3. What is 5 + 3? ")
if answer == "8":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is 8.")

print("\nQuiz Completed!")
print("Your Score is:", score, "/3")    