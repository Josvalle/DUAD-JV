new_order_first = 0
new_order_second = 0

first_number = int(input('Please enter the first number: '))
second_number = int(input('Please enter the second number: '))

if first_number > second_number:
    new_order_first = second_number
    new_order_second = first_number
    print(f'The order of the number enter from lower to higher are: {new_order_first},{new_order_second}')
else:
    print(f'The order of the number enter from lower to higher are: {first_number},{second_number}')