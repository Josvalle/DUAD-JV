print('Welcome to the Age Explorer, where we help you discover your age category')

name = input('Please enter your name: ')
last_name = input('Please enter your last name: ')
age = int(input ('Please enter your age: '))


if age <= 2:
    age_category = 'Baby'
elif age > 2 and age <= 8:
    age_category = 'Kid'
elif age > 8 and age <= 12:
    age_category = 'Preteen'
elif age > 12 and age <= 18:
    age_category = 'Teen'
elif age > 18 and age <= 39:
    age_category = 'Young adult'
elif age > 39 and age <= 64:
    age_category = 'Adult'
elif age > 64:
    age_category = 'Elderly'


print(f'Hi {name} {last_name}, as per your age  you are consider in the category {age_category}.')