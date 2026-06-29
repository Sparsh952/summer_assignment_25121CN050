#1  Write a program to Create library management system


books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully.")

    elif choice == "2":
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])

    elif choice == "3":
        if len(books) == 0:
            print("No books available.")
        else:
            book = input("Enter book name to issue: ")
            if book in books:
                books.remove(book)
                print("Book issued successfully.")
            else:
                print("Book not found.")

    elif choice == "4":
        book = input("Enter book name to return: ")
        books.append(book)
        print("Book returned successfully.")

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")




#2  Write a program to Create bank account system


name = input("Enter account holder name: ")
balance = 0

while True:
    print("\n===== Bank Account System =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited successfully.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == "3":
        print("Account Holder:", name)
        print("Current Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using the Bank Account System.")
        break

    else:
        print("Invalid choice! Please try again.")




#3  Write a program to Create ticket booking system


total_tickets = 10

while True:
    print("\n===== Ticket Booking System =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Available Tickets")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tickets = int(input("Enter number of tickets to book: "))

        if tickets <= total_tickets:
            total_tickets = total_tickets - tickets
            print("Ticket booked successfully.")
        else:
            print("Sorry! Not enough tickets available.")

    elif choice == "2":
        tickets = int(input("Enter number of tickets to cancel: "))
        total_tickets = total_tickets + tickets
        print("Ticket cancelled successfully.")

    elif choice == "3":
        print("Available Tickets:", total_tickets)

    elif choice == "4":
        print("Thank you for using the Ticket Booking System.")
        break

    else:
        print("Invalid choice! Please try again.")        




#4  Write a program to Create contact management system


contacts = {}

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name in contacts:
                print("Name:", name, "- Phone:", contacts[name])

    elif choice == "3":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using the Contact Management System.")
        break

    else:
        print("Invalid choice! Please try again.")        
