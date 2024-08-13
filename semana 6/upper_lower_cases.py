def count_upper_lower_cases(user_string):
    upper_cases = 0
    lower_cases = 0

    for i in user_string:
        if i.isupper():
            upper_cases+=1
        elif i.islower():
            lower_cases+=1
    return upper_cases, lower_cases


def main():
    user_string = input('Please enter a string: ')
    upper, lower = count_upper_lower_cases(user_string)

    print(f'The number of upper letter on the string is {upper} and the number of lower letter is {lower}')

if __name__ == "__main__":
    main()

    