def bubble_sort_list(number_list):
    if type(number_list) == list:
        for first_index in range(len(number_list)):
            for sort_index in range(len(number_list)- first_index - 1):
                if number_list[sort_index] > number_list[sort_index + 1]:
                    print(f"Performing change {number_list[sort_index] } is higher than {number_list[sort_index + 1]}")
                    higher_number = number_list[sort_index]
                    number_list[sort_index] = number_list[sort_index + 1]
                    number_list[sort_index + 1] = higher_number
        return number_list
    raise ValueError('Invalid input!')