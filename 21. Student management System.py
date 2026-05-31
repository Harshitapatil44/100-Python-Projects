students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(student)

def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["Roll No"] == roll_no:
            print("Student Found:")
            print(student)
            return

    print("Student not found.")

def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["Roll No"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")



