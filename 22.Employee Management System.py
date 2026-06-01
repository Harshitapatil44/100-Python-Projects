employees = {}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        employees[emp_id] = {
            "Name": name,
            "Salary": salary
        }
        print("Employee added successfully!")
    elif choice == "2":
        if not employees:
            print("No employees found.")
        else:
            print("\nEmployee Records:")
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}")
                print(f"Name: {details['Name']}")
                print(f"Salary: {details['Salary']}")
                print("-" * 20)
    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in employees:
            print("Employee Found:")
            print(f"Name: {employees[emp_id]['Name']}")
            print(f"Salary: {employees[emp_id]['Salary']}")
        else:
            print("Employee not found.")
          
    elif choice == "4":
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
