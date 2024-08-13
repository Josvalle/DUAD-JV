user_number = int(input('Please enter a number to find if is divisible between 3, 5 or both: '))

if user_number % 3 == 0 and user_number % 5 == 0:
    print('FizzBuzz')
elif user_number % 3 == 0:
    print('Fizz')
elif user_number % 5 == 0:
    print('Buzz')
else:
    print('The number enter is not divisible by 3 or 5')