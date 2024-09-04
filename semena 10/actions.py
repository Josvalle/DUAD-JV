
def loop_to_validate_input(grade_name):
    while  True:
        try:
            grade = int(input(f'Please enter the grade for {grade_name}: '))
            if 0<= grade <=100:
                return grade
            else:
                print('The value for the grade is not between 0 or 100, please try again!')
        except ValueError:
            print('The input enter is not a value number, please enter a number between 0 - 100.')


def student_input():
    average = 0
    complete_name = input('Please enter the student name complete name: ')
    section = input('Please enter the student section: ')
    spanish = loop_to_validate_input('Spanish')
    english = loop_to_validate_input('English')
    history = loop_to_validate_input('History')
    science = loop_to_validate_input('Science')
    average = (spanish + english + history + science)/4


    return {
        'name' : complete_name,
        'section': section,
        'grades':{
            'spanish': spanish,
            'english': english,
            'history': history,
            'science': science
        },
        'average':average
    }

def students_list(students):
    
    exit = 'y'
    while exit == 'y':
        new_student  = student_input()
        students.append(new_student)
        while True:
            exit = input('Do you want to add a new student information? (y/n): ')
            if exit != 'y' and exit != 'n':
                print('Incorrect choose please enter "y" or "n"')
                continue
            else:
                break

    
    return students


def add_new_students(students):
    students_list(students)


def create_dic_average(students):
    name_and_average = []
    for student in students:
        name = student['name']
        average = student['average'] 
        new_dic = { 'name': name, 'average': average}
        name_and_average.append(new_dic)
    return name_and_average


def top_3_students(students):
    try:
        list_averages = create_dic_average(students)
        sorted_list = sorted(list_averages, key=lambda x:x['average'])
        return print(f'The top 3 of students with better average are: first {sorted_list[0]}, second {sorted_list[1]} and for third {sorted_list[2]}')
    except IndexError:
        print('There is not enough students to show the top 3, please add more students.')


def obtain_list_average(students):
    averages = []
    for student in students:  
        new_average = float(student['average'])  
        averages.append(new_average)
    all_student_average = sum(averages) / len(averages) 
    return print(f'The average of all the averages of the students inputs is: {all_student_average}')











