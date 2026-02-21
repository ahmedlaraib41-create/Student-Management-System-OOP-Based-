class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "D"

    def display_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        print("-" * 20)
        

students = []

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
    
    student = Student(student_id, name, age, marks)
    students.append(student)
    print("Student added successfully\n")

def view_students():
    if not students:
        print("No students found\n")
    else:
        for student in students:
            student.display_info()

def search_student():
    search_id = input("Enter student ID to search: ")
    for student in students:
        if student.student_id == search_id:
            student.display_info()
            return
    print("Student not found\n")

def update_student():
    search_id = input("Enter student ID to update: ")
    for student in students:
        if student.student_id == search_id:
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.marks = float(input("Enter new marks: "))
            print("Student updated\n")
            return
    print("Student not found\n")

def delete_student():
    search_id = input("Enter student ID to delete: ")
    for student in students:
        if student.student_id == search_id:
            students.remove(student)
            print("Student deleted\n")
            return
    print("Student not found\n")

def menu():
    while True:
        print("===== Student Management System =====")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Update Student")
        print("5 Delete Student")
        print("6 Exit") 

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
            print("Invalid choice\n")

menu()
