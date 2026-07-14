# INPUT
users = {
    'ccab':  {'password': '1234', 'role': 'student',     'name': 'Cristian Cab'},
    'aleher': {'password': '1234', 'role': 'student',     'name': 'Alejandro Hernandez'},
    'ivanr': {'password': '1234', 'role': 'student',     'name': 'Ivan Rivas'},
    'keyrap':  {'password': '1234', 'role': 'student',     'name': 'Keyra Pool'},
    'euc':     {'password': '1234', 'role': 'student',     'name': 'Ernesto Uc'},
    'cbalam':  {'password': '1234', 'role': 'student',     'name': 'Carlos Balam'},
    'jpedrozo':{'password': '1234', 'role': 'teacher',     'name': 'Jorge Pedrozo'},
    'rgarcia': {'password': '1234', 'role': 'coordinator', 'name': 'Rosa García'}
}

subjects = ('Mathematics', 'Programming', 'English')

grades = {
    'ccab':  {'Mathematics': 8.5, 'Programming': 9.0, 'English': 7.5},
    'aleher': {'Mathematics': 9.0, 'Programming': 8.0, 'English': 8.5},
    'ivanr': {'Mathematics': 7.5, 'Programming': 8.0, 'English': 8.5},
    'keyrap':  {'Mathematics': 9.5, 'Programming': 9.8, 'English': 9.2},
    'euc':     {'Mathematics': 8.2, 'Programming': 6.9, 'English': 8.8},
    'cbalam':  {'Mathematics': 8.8, 'Programming': 9.0, 'English': 8.5}
}


class InvalidGradeError(Exception):
    pass


# PROCESS
access_granted = False
current_user = ''

while access_granted == False:
    username = input('Username: ')
    password = input('Password: ')

    if username in users and users[username]['password'] == password:
        access_granted = True
        current_user = username
    else:
        # OUTPUT
        print('Invalid username or password. Please try again.\n')

current_name = users[current_user]['name']
current_role = users[current_user]['role']

# OUTPUT
print('\nWelcome, ' + current_name + ' (' + current_role.capitalize() + ')')
print('=' * 40)

# PROCESS
if current_role == 'student':

    print('Report Card for ' + current_name)
    print('-' * 40)

    passed_subjects = set()

    for subject in subjects:
        grade = grades[current_user][subject]
        print(subject + ': ' + str(grade))

        if grade >= 8.0:
            passed_subjects.add(subject)

    pending_subjects = set(subjects) - passed_subjects

    print('\nPassed subjects: ' + str(passed_subjects))
    print('Pending subjects: ' + str(pending_subjects))

elif current_role == 'teacher':

    print('Student List:')
    print('-' * 40)

    for username in users:
        if users[username]['role'] == 'student':
            print(username.ljust(10) + ' | ' + users[username]['name'])

    continue_grading = True

    while continue_grading == True:
        print()

        student = input('Student username (or type "Exit" to quit): ')

        if student == 'Exit':
            continue_grading = False
        else:
            if student in grades:

                subject = input('Subject: ')

                if subject in subjects:

                    current_grade = grades[student][subject]

                    try:
                        new_grade_input = input('New grade: ')
                        new_grade = float(new_grade_input)

                        if new_grade < 0 or new_grade > 10:
                            raise InvalidGradeError(
                                'Error: The grade must be between 0 and 10.'
                            )

                    except ValueError:
                        print('Error: The grade must be a number.')

                    except InvalidGradeError as e:
                        print(e)

                    else:
                        print('Current grade: ' + str(current_grade))
                        print('New grade: ' + str(new_grade))
                        confirmation = input('Confirm change? (yes/no): ')

                        if confirmation == 'yes':
                            grades[student][subject] = new_grade
                            print('Grade updated.')
                        else:
                            print('Change canceled.')
                else:
                    print('Invalid subject.')
            else:
                print('Student not found.')

elif current_role == 'coordinator':

    print('Teacher List:')
    print('-' * 40)

    for username in users:
        if users[username]['role'] == 'teacher':
            print(username.ljust(10) + ' | ' + users[username]['name'])

    print('\nSubject List:')
    print('-' * 40)

    for subject in subjects:
        print(subject)

    print('\nStudent List with Grades:')
    print('-' * 90)

    header = 'Subject'.ljust(15)
    for username in grades:
        header = header + users[username]['name'].ljust(20)
    print(header)
    print('-' * 90)

    for subject in subjects:
        row = subject.ljust(15)
        for username in grades:
            grade = grades[username][subject]
            grade_text = str(grade)
            if grade < 8.0:
                grade_text = grade_text + ' (F)'
            row = row + grade_text.ljust(20)
        print(row)

else:
    print('Access type not recognized.')

# AI DECLARATION
# I used AI to help me understand and improve my code, and to add error handling.
