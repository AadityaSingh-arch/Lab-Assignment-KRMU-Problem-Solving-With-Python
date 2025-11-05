# Gradebook Analyzer
# Name : Aaditya Singh
# Course: B.tech CSE( full stack development)
# Roll no. : 2501350057
# Assign. Desc. : A python code for analyzing student grades
print("----------------------------------")
print("Welcome to the Gradebook Analyzer!")
print("----------------------------------")


while True:
    try:
        num_students = int(input("Enter the number of students: "))
        if num_students < 0:
            print("Please enter 0 or a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a whole number (e.g. 3).")

while True:
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects < 0:
            print("Please enter 0 or a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a whole number (e.g. 4).")


subject_names = []
for i in range(num_subjects):

    name = input(f"Name of subject {i+1}: ").strip()
    if name == "":
        name = f"Subject{i+1}"
    subject_names.append(name)

marks = {}  
for i in range(num_students):
    student = input(f"Enter name of student {i+1}: ").strip()
    
    if student == "":
        student = f"Student{i+1}"
    marks[student] = {}
    for subject in subject_names:
        while True:
            try:
                score = float(input(f"Enter marks for {student} in {subject}: "))
                
                if score < 0 or score > 100:
                    print("Please enter a number between 0 and 100 for marks.")
                    continue
                break
            except ValueError:
                print("Please enter a number (e.g. 75 or 82.5).")
        marks[student][subject] = score


totals = {}
averages = {}
for student, smarks in marks.items():
    total = 0
    for subject in subject_names:
        total += smarks.get(subject, 0)
    totals[student] = total
    if len(subject_names) > 0:
        averages[student] = total / len(subject_names)
    else:
        averages[student] = 0


if len(averages) > 0:
    class_average = sum(averages.values()) / len(averages)
else:
    class_average = 0


grades = {}
for student, avg in averages.items():
    if avg >= 90:
        grades[student] = 'A'
    elif avg >= 80:
        grades[student] = 'B'
    elif avg >= 70:
        grades[student] = 'C'
    elif avg >= 60:
        grades[student] = 'D'
    else:
        grades[student] = 'F'


passed_students = [s for s, a in averages.items() if a >= 40]
failed_students = [s for s, a in averages.items() if a < 40]

def print_results_table():

    if not marks:
        print("No student data.")
        return

    header = "Student"
    for sub in subject_names:
        header += "\t" + sub
    header += "\tTotal\tAverage\tGrade"
    print('\n' + header)
    print('-' * 60)

    for student in marks:
        row = student
        for sub in subject_names:
            row += "\t" + str(marks[student].get(sub, 0))
        row += "\t" + str(totals.get(student, 0))
        row += "\t" + str(round(averages.get(student, 0), 2))
        row += "\t" + grades.get(student, '-')
        print(row)

def print_class_stats():
    print('\nClass Average (mean of student averages):', round(class_average, 2))
    if totals:
        best = max(totals, key=totals.get)
        worst = min(totals, key=totals.get)
        print('Highest total:', totals[best], '->', best)
        print('Lowest total:', totals[worst], '->', worst)

def print_pass_fail():
    print('\nPassed students:', passed_students)
    print('Failed students:', failed_students)


print_results_table()


while True:
    print('\nMenu:')
    print('1) Show results table')
    print('2) Show class statistics')
    print('3) Show pass/fail lists')
    print('4) Exit')
    choice = input('Choose (1-4): ').strip()
    if choice == '1':
        print_results_table()
    elif choice == '2':
        print_class_stats()
    elif choice == '3':
        print_pass_fail()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Please enter 1, 2, 3 or 4.')
