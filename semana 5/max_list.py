number_list=[]

for i in range(10):
    user_number = int(input('Please enter a number: '))
    number_list.append(user_number)

highest_number = max(number_list)
print(f'The numbers your enter are {number_list}, and the highest number is: {highest_number}')