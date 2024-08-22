number_list = []

for i in range (3):
    user_number = int(input('Please enter a number: '))
    number_list.append(user_number)

sum_list = sum(number_list)

if 30 in number_list:
    print('Correct')
elif sum_list == 30:
    print('Correct')
else:
    print('Incorrect')
