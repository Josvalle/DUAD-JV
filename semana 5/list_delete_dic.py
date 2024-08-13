employee_info = {
    'Employee ID': 'E12345',
    'First Name': 'John',
    'Last Name': 'Doe',
    'Position': 'Software Engineer',
    'Department': 'IT',
    'Salary': '$85,000',
    'Hire Date': '2020-01-15'
}

delete_list =['Hire Date','Employee ID']

for index, value in enumerate(delete_list):
        delete_value = employee_info.pop(value)
        

print(employee_info)