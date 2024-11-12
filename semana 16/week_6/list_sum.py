def list_request_for_user():
    number_list = []
    exit = 'y'
    while exit == 'y':
        number = int(input('Please entre a number: '))
        number_list.append(number)
        print(number_list)
        exit=input('Do you want to add another number (y/n) ')

        if exit == 'n':
            return number_list


def sum_of_list_number(number_list):
    sum_list = sum(number_list)
    return sum_list

def main():
    number_list = list_request_for_user()
    sum_of_numbers = sum_of_list_number(number_list)
    print(sum_of_numbers)


if __name__ == "__main__":
    main()