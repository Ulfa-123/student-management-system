students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        mark = input("Enter mark: ")

        students.append({
            "name": name,
            "mark": mark
        })

        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent Records")

        for student in students:
            print(f"Name: {student['name']}, Mark: {student['mark']}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
