grade_list = []
approve_list = []
fail_list= []
quantity_grades = int(input('Please enter how many grade will you enter on the system: '))

for i in range(quantity_grades):
    count = i + 1
    user_grade = int(input(f'Please enter the grade {count}: '))
    grade_list.append(user_grade)
    if user_grade >= 70:
        approve_list.append(user_grade)
    else:
        fail_list.append(user_grade)

sum_grades = sum(grade_list)
sum_approve_grades = sum(approve_list)
sum_fail_grades = sum(fail_list)
amount_approve = len(approve_list)
amount_fails = len(fail_list)

average_grade = sum_grades/quantity_grades
average_approve = sum_approve_grades/amount_approve
average_fails = sum_fail_grades/amount_fails


print(f'''The average of all your grades is {average_grade}, 
you have a amount of approve grade of {amount_approve} with the average of {average_approve} 
and amount of fails grade of {amount_fails} with the average of  {average_fails}''')