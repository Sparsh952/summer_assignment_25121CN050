#1  Write a program to Create menu-driven calculator


while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Calculator Closed.")
        break

    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
            print("Addition =", result)

        elif choice == 2:
            result = num1 - num2
            print("Subtraction =", result)

        elif choice == 3:
            result = num1 * num2
            print("Multiplication =", result)

        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print("Division =", result)
            else:
                print("Error! Division by zero is not allowed.")

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")




#2  Write a program to Create menu-driven array operations system


arr = []

while True:
    print("\n===== ARRAY MENU =====")
    print("1. Add Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Find Maximum")
    print("6. Find Minimum")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        num = int(input("Enter element to add: "))
        arr.append(num)
        print("Element added successfully.")

    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array:", arr)

    elif choice == 3:
        num = int(input("Enter element to search: "))
        if num in arr:
            print("Element found at index", arr.index(num))
        else:
            print("Element not found.")

    elif choice == 4:
        num = int(input("Enter element to delete: "))
        if num in arr:
            arr.remove(num)
            print("Element deleted successfully.")
        else:
            print("Element not found.")

    elif choice == 5:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Maximum element =", max(arr))

    elif choice == 6:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Minimum element =", min(arr))

    elif choice == 7:
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")        




#3  Write a program to Create menu-driven string operations system.        


text = input("Enter a string: ")

while True:
    print("\n===== STRING MENU =====")
    print("1. Display String")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Reverse String")
    print("5. Find Length")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("String:", text)

    elif choice == 2:
        print("Uppercase:", text.upper())

    elif choice == 3:
        print("Lowercase:", text.lower())

    elif choice == 4:
        print("Reversed String:", text[::-1])

    elif choice == 5:
        print("Length of String:", len(text))

    elif choice == 6:
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")




#4  Write a program to Create inventory management system


inventory = {}

while True:
    print("\n===== INVENTORY MENU =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory[item] = quantity
        print("Item added successfully.")

    elif choice == 2:
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("\nInventory:")
            for item, quantity in inventory.items():
                print(item, ":", quantity)

    elif choice == 3:
        item = input("Enter item name to update: ")
        if item in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[item] = quantity
            print("Quantity updated successfully.")
        else:
            print("Item not found.")

    elif choice == 4:
        item = input("Enter item name to delete: ")
        if item in inventory:
            del inventory[item]
            print("Item deleted successfully.")
        else:
            print("Item not found.")

    elif choice == 5:
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")        
