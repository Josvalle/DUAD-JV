def digit_checker(func):
    def wrapper(*args):
        for index, arg in enumerate(args):
            if arg.isdigit():
                pass
            else:
                raise ValueError(f"The Value enter '{arg}' is not a digits, please enter only digits")
        func(*args)
    return wrapper


def list_request_for_user(number_list):
    exit = 'y'
    while exit == 'y':
        number = input('Please entre a number: ')
        number_list.append(number)
        print(number_list)
        exit=input('Do you want to add another number (y/n) ')

        if exit == 'n':
            return number_list

@digit_checker
def sum_of_list_number(*args):
    new_list = []
    for index, values in enumerate(args):
        new_value = int(values)
        new_list.append(new_value)
    return print(f'The sum of all the number enter is {sum(new_list)}')

def main():
    number_list = []
    number_list_1 = list_request_for_user(number_list )
    sum_of_numbers = sum_of_list_number(*number_list_1)


if __name__ == "__main__":
    main()