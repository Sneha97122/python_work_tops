
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def add(students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))
    grade = grade(marks)
    students.append({"name": name, "marks": marks, "grade": grade})
    print("Record added successfully!\n")


def display(students):
    if not students:
        print("No student records found!\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")
        print()


def main():
    students = []

    while True:
        print("===== Grade Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add(students)

        elif choice == "2":
            display(students)

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.\n")

# Run the program
main()
 
