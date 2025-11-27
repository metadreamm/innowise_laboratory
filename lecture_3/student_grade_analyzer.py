students = []

while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new sudent")
    print("2. Add a grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")

    try:
        choice = int(input("Enter your choise: "))
    except ValueError:
        print("Please enter a number")
        continue

    # Option 1: Add a new student
    if choice == 1:
        name = input("Enter student name: ").strip()
        # Check if this student already exists
        exists = False
        for x in students:
            if x["name"] == name:
                exists = True
                break
        
        if exists:
            print("This student already exists.")
        else:
            students.append({"name": name, "grades": []})
            print("SUCCESS")
    
    # Option 2. Add grades for a student
    elif choice == 2:
        name = input("Enter student name: ").strip()

        # Find the student
        student = None
        for x in students:
            if x["name"] == name:
                student = x
                break

        if student is None:
            print("Student not found")
        else:
            while True:
                grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
                if grade_input == "done":
                    break

                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                        print("SUCCESS")
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'done'")

    # Option 3. Show report (all students)
    elif choice == 3:
        if not students:
            print("No students to show")
        else:
            # Store averages for summary
            student_averages = []

            for x in students:
                grades = x["grades"]

                try:
                    avg = sum(grades) / len(grades)
                except ZeroDivisionError:
                    # No grades
                    avg = None

                if avg is None:
                    print(f"{x['name']}'s average grade is N/A")
                else: 
                    print(f"{x['name']}'s average grade is {avg:.2f}")
                    student_averages.append(avg)

            # Overall summary
            if not student_averages:
                print("There are no grades at all")
            else:
                max_avg = max(student_averages)
                min_avg = min(student_averages)
                overall_avg = sum(student_averages) / len(student_averages)
                print(f"Max average: {max_avg:.2f}")
                print(f"Min average: {min_avg:.2f}")
                print(f"Overall average: {overall_avg:.2f}")

    # Option 4. Find top performer
    elif choice == 4:
        if not students:
            print("No students yet")
        else:
            # Calculate the avg grade inside the lambda
            # if there are no grades - return 0
            def avg_or_zero(student):
                grades = student["grades"]
                if not grades:
                    return 0
                return sum(grades) / len(grades)
            
            # Check whether there is at least one grade at all
            if all(len(x["grades"]) == 0 for x in students):
                print("No grades added yet")
            else:
                top_student = max(students, key=lambda x: avg_or_zero(x))
                top_avg = avg_or_zero(top_student)
                print(f"Top performer: {top_student['name']} with average {top_avg:.2f}")

    elif choice == 5:
        print("Exiting program")
        break

