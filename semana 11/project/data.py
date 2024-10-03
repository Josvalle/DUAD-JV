import csv
from actions import convert_class_dic
from actions import convert_dict_class
def create_csv_file(file_path,students,students_headers):
    with open(file_path, 'w', encoding='utf=8') as file:
        writer = csv.DictWriter(file, fieldnames=students_headers)
        writer.writeheader()
        writer.writerows(students)

def export_csv(students):
    
    students_headers = (
        'name',
        'section',
        'spanish',
        'english',
        'history',
        'science',
        'average'
    )
    convert_student_list = convert_class_dic(students)
    create_csv_file('students.csv',convert_student_list, students_headers)


def import_csv_file(file_path,students):
    
    try:
        
        with open(file_path,'r') as file:
            reader_of_file = csv.DictReader(file)
            list_of_dicts = list(reader_of_file)
        
        convert_student_list = convert_dict_class (list_of_dicts)
        students.extend(convert_student_list)
        return students
    except FileNotFoundError:
        print('There is not file no import yet, please first export a file')

