counter = 1
sum_number = 0

user_number = int(input('Please enter a number: '))

for i in range(user_number):
    sum_number = sum_number + counter
    counter = counter + 1


print(sum_number)