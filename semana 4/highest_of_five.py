number_list = []

for i in range(5):
    user_number = int(input('Please enter a number: '))
    number_list.append(user_number)

highest_number = max(number_list)
print(f'The highest number enter is {highest_number}')
