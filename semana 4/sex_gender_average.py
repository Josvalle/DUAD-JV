counter_men = 0
counter_women = 0

for i in range(6):
    gender = int(input('Please enter the gender 1 if man / 2 if woman: '))
    if gender == 1:
        counter_men = counter_men + 1
    else:
        counter_women = counter_women + 1

percentage_men = (counter_men*100)/6
percentage_women = (counter_women*100)/6

print(f'The percentage of men enter is {percentage_men} and the percentage of women is {percentage_women}')