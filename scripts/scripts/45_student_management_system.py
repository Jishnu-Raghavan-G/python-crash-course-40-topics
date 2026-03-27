students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()


def search_student():
    name = input("Enter name to search: ")

    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:")
            print(student)
            found = True
            break

    if not found:
        print("Student not found.\n")


def delete_student():
    name = input("Enter name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student removed.\n")
            return

    print("Student not found.\n")


def update_student():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Leave blank to keep old value")

            new_name = input("New name: ")
            new_age = input("New age: ")
            new_grade = input("New grade: ")

            if new_name:
                student["name"] = new_name
            if new_age:
                student["age"] = int(new_age)
            if new_grade:
                student["grade"] = new_grade

            print("Student updated.\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.\n")


menu()
