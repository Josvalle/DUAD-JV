number_list = []
position = 0
for i in range(100):
    position = position + 1
    user_number = int(input(f'Please enter a number Position = ({position}) :  '))
    number_list.append(user_number)

sum_number = sum(number_list)

print(f'The sum of all the 100 number enter is: {sum_number}')