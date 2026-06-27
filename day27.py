#1  Write a program to Create student record management system


students = []

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student record added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print("Roll No:", student["roll"])
                print("Name    :", student["name"])
                print("Marks   :", student["marks"])
                print("------------------------")

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print("Roll No:", student["roll"])
                print("Name   :", student["name"])
                print("Marks  :", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to delete: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student record deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")




#2  Write a program to Create employee management system


employees = []

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")

        employee = {
            "id": emp_id,
            "name": name,
            "salary": salary
        }

        employees.append(employee)
        print("Employee added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for employee in employees:
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Salary      :", employee["salary"])
                print("--------------------------")

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        found = False

        for employee in employees:
            if employee["id"] == emp_id:
                print("\nEmployee Found")
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Salary      :", employee["salary"])
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to delete: ")
        found = False

        for employee in employees:
            if employee["id"] == emp_id:
                employees.remove(employee)
                print("Employee deleted successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "5":
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")        




#3  Write a program to Create salary management system


salary_records = []

while True:
    print("\n--- Salary Management System ---")
    print("1. Add Salary Record")
    print("2. View All Salary Records")
    print("3. Search Salary Record")
    print("4. Delete Salary Record")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Monthly Salary: ")

        record = {
            "id": emp_id,
            "name": name,
            "salary": salary
        }

        salary_records.append(record)
        print("Salary record added successfully!")

    elif choice == "2":
        if len(salary_records) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records:")
            for record in salary_records:
                print("Employee ID :", record["id"])
                print("Name        :", record["name"])
                print("Salary      :", record["salary"])
                print("--------------------------")

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        found = False

        for record in salary_records:
            if record["id"] == emp_id:
                print("\nSalary Record Found")
                print("Employee ID :", record["id"])
                print("Name        :", record["name"])
                print("Salary      :", record["salary"])
                found = True
                break

        if not found:
            print("Salary record not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to delete: ")
        found = False

        for record in salary_records:
            if record["id"] == emp_id:
                salary_records.remove(record)
                print("Salary record deleted successfully!")
                found = True
                break

        if not found:
            print("Salary record not found.")

    elif choice == "5":
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")       




#4  Write a program to Create marksheet generation system


print("----- Marksheet Generation System -----")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Marksheet -----")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)        