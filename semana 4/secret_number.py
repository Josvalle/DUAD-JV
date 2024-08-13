import random
import time
import os
user_number = 0
secret_number = random.randint(1,10)

while user_number != secret_number:
    user_number=int(input('Please enter a number between 1 and 10 to guess the secret number: '))
    if user_number == secret_number:
        break
    else:
        print('Incorrect number please enter guess again')
        time.sleep(2)
        os.system("cls")

print(f'You win!!, the number was {secret_number}')