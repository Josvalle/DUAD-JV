def loop_to_validate_input():
    while  True:
        try:
            number = int(input(f'Please enter a number between the 0 - 100: '))
            if 0<= number <=100:
                return number
            else:
                print('The value for the grade is not between 0 or 100, please try again!')
        except ValueError:
            print('The input enter is not a value number, please enter a number between 0 - 100.')


def request_numbers(number_list):
    while True:
        number = loop_to_validate_input()
        number_list.append(number)
        exit = input('Do you want to add another number? (Y/N): ')
        try:
            if exit == "N" or exit == 'n':
                break
        except:
            print('Incorrect Value enter please select (Y/N)')
    return number_list


def bubble_sort_list(number_list):
    for first_index in range(len(number_list)):
        for sort_index in range(len(number_list)- first_index - 1):
            if number_list[sort_index] > number_list[sort_index + 1]:
                print(f"Performing change {number_list[sort_index] } is higher than {number_list[sort_index + 1]}")
                higher_number = number_list[sort_index]
                number_list[sort_index] = number_list[sort_index + 1]
                number_list[sort_index + 1] = higher_number
    return number_list



def main():
    number_list = []
    unsorted_list = request_numbers(number_list)
    sorted_list =bubble_sort_list(unsorted_list)
    print(sorted_list)

if __name__ == "__main__":
    main()