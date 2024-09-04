
from actions import add_new_students
from actions import obtain_list_average
from actions import top_3_students
from data import export_csv
from data import import_csv_file




def menu_options(students):
    while True: 
        selection = input('''

        1 = Add new student
        2 = Check information of the students add it
        3 = See top 3 student grades 
        4 = See the average notes of all students 
        5 = Export all data to a CSV file 
        6 = Import all data from a previous CSV file 
        7 = Exit the program


    Your selection: ''')

        if selection == '1':
            add_new_students(students)
        elif selection == '2':
            print(students)
        elif selection == '3':
            top_3_students(students)
        elif selection == '4':
            obtain_list_average(students)
        elif selection == '5':
            export_csv(students)
        elif selection == '6':
            import_csv_file('students.csv',students)
        elif selection == '7':
            break
        else:
            print('Please select a valid option!')