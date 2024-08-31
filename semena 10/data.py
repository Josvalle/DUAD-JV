import csv

def create_csv_file(file_path,students,students_headers):
    with open(file_path, 'w', encoding='utf=8') as file:
        writer = csv.DictWriter(file, fieldnames=students_headers)
        writer.writeheader()
        writer.writerows(students)

def export_csv(students):
    students_headers=(
        'name',
        'section',
        'grades',
        'average'
    )
    create_csv_file('students.csv',students, students_headers)


def import_csv_file(file_path,students):
    
    try:
        
        with open(file_path,'r') as file:
            reader_of_file = csv.DictReader(file)
            list_of_dicts = list(reader_of_file)
        students.extend(list_of_dicts)
        return students
    except FileNotFoundError:
        print('There is not file no import yet, please first export a file')

