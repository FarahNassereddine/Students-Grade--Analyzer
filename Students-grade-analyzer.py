# Function to enter student names and grades using recursion
def get_students_data(n, names=[], grades=[], index=0):
    if index == n:
        return names, grades
    else:
        name = input(f"Enter name of student f{index + 1}: ")
        
        # Loop until a valid grade is entered
        grade = -1  # Initialize grade to an invalid value
        while grade < 0 or grade > 100:
            grade_input = input ("Enter grade of :"),{name} ,("out of 100): ")
            if grade_input.replace('.', '', 1).isdigit():  # Check if input is a number
                grade = float(grade_input)
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100. Please try again.")
            else:
                print("Invalid input. Please enter a numeric value.")
        
        names.append(name)
        grades.append(grade)
        return get_students_data(n, names, grades, index + 1)

# Function to display all student names and grades
def display_student_summary(names, grades):
    print("\n--- Student Summary ---")
    for i in range(len(names)):
        print(f"{names[i]}: {grades[i]}")

# Function to get average grade
def get_avg_grade(grades):
    if len(grades) == 0:
        return 0
    total = sum(grades)
    avg = total / len(grades)
    return avg

# Function to get highest grade and corresponding student
def get_heighest_grade(names, grades):
    if len(grades) == 0:
        return None, 0
    max_grade = max(grades)
    index = grades.index(max_grade)
    return names[index], max_grade

# Function to count students who passed
def count_passed(grades):
    return sum(1 for grade in grades if grade >= 60)

# Main program
def main():
    num_students = int(input("Enter the number of students: "))
    if num_students <= 0:
        print("No students to process.")
        return

    names, grades = get_students_data(num_students)

    display_student_summary(names, grades)

    avg = get_avg_grade(grades)
    print ("\n Class average grade:", {avg:.2})

    top_student, top_grade = get_heighest_grade(names, grades)
    if top_student:
        print("Highest grade: ",{top_grade} ,("earned by ",{top_student}))
    else:
        print("No grades available to determine the highest grade.")

    passed_count = count_passed(grades)
    print("Number of students who passed:" ,{passed_count})

# Run the main program
if __name__ == "__main__":
    main()
