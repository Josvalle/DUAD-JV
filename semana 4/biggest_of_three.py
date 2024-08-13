number_list = []
highest_number = 0 
for i in range(3):
    user_number = int(input('Please enter a number: '))
    number_list.append(user_number)
    if user_number > highest_number:
        highest_number = user_number



print(f'The highest number enter is: {highest_number}')
