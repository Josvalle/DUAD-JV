seconds = int(input('Please enter the amount of seconds: '))

if seconds > 600:
    print("higher")
else:
    missing_seconds = seconds - 600
    print(f'The amount of second missing to reach the 10 minutes is {missing_seconds}')
