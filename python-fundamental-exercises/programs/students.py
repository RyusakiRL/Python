students = {}

def student(act, students_dictionary, name, grade):
    if act == "add":
        new_student = {
            "Student": name,
            "Grade": grade
        }
        students.append(new_student)

    elif act == "search":
        for student in students_dictionary:

            if student["Student"] == name:
                print(f"Your grade is: {student['Grade']}" )
        
    
    elif act == "remove":
        for student in students_dictionary:

            if student["Student"] == name:
                del student["Student"]
                del student["Grade"]
            else:
                print("This student don't exists")
    print(f"{students}")

while True:
    print("\n----------------MAIN SCHOOL----------------\n")
    action = input("Type: 'add', 'remove', 'search' or 'exit'\n")
    
    if action == "exit": break
    
    elif action == "add":
        nam = input(("Insert the student name\n"))
        note = float(input("Insert the exam grade\n"))
        student(action, students, nam, note)

    elif action == "remove":
        nam = input(("Insert the student name\n"))
        student(action, students, nam, 0);

    elif action == "search":
        nam = input(("Insert the student name\n"))
        student(action, students, nam, 0);

    else:
        print("Invalid command!!");
