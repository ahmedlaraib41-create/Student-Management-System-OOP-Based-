# Student Management System

A simple *Python console application* to manage student records using *Object-Oriented Programming (OOP)*.  
This project allows users to *add, view, search, update, and delete student records*, and automatically calculates grades based on marks.  

It is a beginner-friendly project ideal for learning Python classes, lists, and CRUD operations.

---

## Features

- Add a new student with *ID, Name, Age, and Marks*
- View all student records with calculated grades
- Search a student by *ID*
- Update student details (Name, Age, Marks)
- Delete a student record
- Automatically calculate *grades* based on marks:
  - 90+ → A
  - 80–89 → B
  - 70–79 → C
  - Below 70 → D
- Console-based menu interface for easy navigation

---

## Program Structure

1. *Student Class*
   - Attributes: student_id, name, age, marks
   - Methods:  
     - display_info() → prints student details and grade  
     - calculate_grade() → calculates grade based on marks  

2. *Main Menu Function*
   - Displays menu options 1–6:
     1. Add Student
     2. View Students
     3. Search Student
     4. Update Student
     5. Delete Student
     6. Exit
   - Uses a while True loop to keep the program running until the user exits

3. *Data Storage*
   - students = [] list to store student objects
   - Each item in the list is a Student object

---

## Future Improvements

- Save student data to a *CSV or JSON file* so it persists between program runs
- Add *duplicate ID check* when adding a student
- Include *input validation* for age and marks
- Implement a *GUI interface* using Tkinter or PyQt
- Add functionality to *sort students* by name, marks, or grade

---

## Contributing

Feel free to fork this repository, make changes, and submit pull requests.  
Any feedback or suggestions are welcome!

---

## License

This project is *open source* and free to use.
