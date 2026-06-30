#1  Write a program to Create student record sysem using array and string


names = []
roll_numbers = []
marks = []

while True:
    print("\n----- Student Record System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        mark = input("Enter marks: ")

        names.append(name)
        roll_numbers.append(roll)
        marks.append(mark)

        print("Student record added successfully!")

    elif choice == "2":
        if len(names) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for i in range(len(names)):
                print("Name:", names[i])
                print("Roll No:", roll_numbers[i])
                print("Marks:", marks[i])
                print("----------------------")

    elif choice == "3":
        search_roll = input("Enter roll number to search: ")

        found = False
        for i in range(len(roll_numbers)):
            if roll_numbers[i] == search_roll:
                print("\nStudent Found:")
                print("Name:", names[i])
                print("Roll No:", roll_numbers[i])
                print("Marks:", marks[i])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Exiting Student Record System...")
        break

    else:
        print("Invalid choice! Please try again.")




#2  Write a program to Create mini library system


books = []

while True:
    print("\n----- Mini Library System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])

    elif choice == "3":
        book = input("Enter book name to search: ")

        if book in books:
            print("Book found in the library.")
        else:
            print("Book not found.")

    elif choice == "4":
        book = input("Enter book name to remove: ")

        if book in books:
            books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Exiting Mini Library System...")
        break

    else:
        print("Invalid choice! Please try again.")




#3  Write a program to Create mini employee management system


emp_names = []
emp_ids = []
emp_salaries = []

while True:
    print("\n----- Mini Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        salary = input("Enter employee salary: ")

        emp_names.append(name)
        emp_ids.append(emp_id)
        emp_salaries.append(salary)

        print("Employee added successfully!")

    elif choice == "2":
        if len(emp_names) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for i in range(len(emp_names)):
                print("Name   :", emp_names[i])
                print("ID     :", emp_ids[i])
                print("Salary :", emp_salaries[i])
                print("------------------------")

    elif choice == "3":
        search_id = input("Enter employee ID to search: ")

        found = False
        for i in range(len(emp_ids)):
            if emp_ids[i] == search_id:
                print("\nEmployee Found:")
                print("Name   :", emp_names[i])
                print("ID     :", emp_ids[i])
                print("Salary :", emp_salaries[i])
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        remove_id = input("Enter employee ID to remove: ")

        found = False
        for i in range(len(emp_ids)):
            if emp_ids[i] == remove_id:
                emp_names.pop(i)
                emp_ids.pop(i)
                emp_salaries.pop(i)
                print("Employee removed successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "5":
        print("Exiting Employee Management System...")
        break

    else:
        print("Invalid choice! Please try again.")        




#4  Write a program to Develop complete mini project using arrays, strings and functions.

# Mini Project: Student Management System


names = []
roll_numbers = []
marks = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    mark = input("Enter marks: ")

    names.append(name)
    roll_numbers.append(roll)
    marks.append(mark)

    print("Student added successfully!")


def display_students():
    if len(names) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records")
        print("----------------------------")
        for i in range(len(names)):
            print("Name :", names[i])
            print("Roll :", roll_numbers[i])
            print("Marks:", marks[i])
            print("----------------------------")


def search_student():
    roll = input("Enter roll number to search: ")

    found = False
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == roll:
            print("\nStudent Found")
            print("Name :", names[i])
            print("Roll :", roll_numbers[i])
            print("Marks:", marks[i])
            found = True
            break

    if found == False:
        print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")

    found = False
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == roll:
            names.pop(i)
            roll_numbers.pop(i)
            marks.pop(i)
            print("Student deleted successfully!")
            found = True
            break

    if found == False:
        print("Student not found.")


# Main Program
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you! Program Ended.")
        break

    else:
        print("Invalid choice! Try again.")

        
