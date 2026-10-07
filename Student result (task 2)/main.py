
# A simple program that shows a student's result.

def get_student_info():
    """Ask the user for the student's name and marks."""
    name = input("Enter student name: ")
    marks = []
    number_of_subjects = int(input("How many subjects? "))

    for i in range(number_of_subjects):
        mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
        marks.append(mark)

    return name, marks


def calculate_total(marks):
    """Add up all the marks."""
    return sum(marks)


def calculate_average(marks):
    """Find the average of the marks."""
    return sum(marks) / len(marks)


def find_grade(average):
    """Give a grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"


def find_status(average):
    """Pass if the average is 50 or more, otherwise Fail."""
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def show_result(name, total, average, grade, status):
    """Print the final result."""
    print()
    print("----- Student Result -----")
    print("Name   :", name)
    print("Total  :", total)
    print("Average:", round(average, 2))
    print("Grade  :", grade)
    print("Status :", status)
    print("--------------------------")


def process_student():
    """Run the whole program step by step."""
    name, marks = get_student_info()

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = find_grade(average)
    status = find_status(average)

    show_result(name, total, average, grade, status)


process_student()