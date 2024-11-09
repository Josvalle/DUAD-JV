def loop_to_validate_input(): # O(1)
    while  True: # O(1)  
        try:
            number = int(input(f'Please enter a number between the 0 - 100: ')) #0(1)
            if 0<= number <=100:#0(1)
                return number #0(1)
            else:
                print('The value for the grade is not between 0 or 100, please try again!') #0(1)
        except ValueError:
            print('The input enter is not a value number, please enter a number between 0 - 100.') #0(1)


def request_numbers(number_list):
    while True: # O(n)
        number = loop_to_validate_input() # O(1)
        number_list.append(number)  # O(1)
        exit = input('Do you want to add another number? (Y/N): ') # O(1)
        try:
            if exit == "N" or exit == 'n': # O(1)
                break # O(1)
        except:
            print('Incorrect Value enter please select (Y/N)') # O(1)
    return number_list # O(1)


def bubble_sort_list(number_list): # O(n^2)
    for first_index in range(len(number_list)): #O(n)
        for sort_index in range(len(number_list)- first_index - 1): # O(n^2)
            if number_list[sort_index] > number_list[sort_index + 1]: # O(1)
                print(f"Performing change {number_list[sort_index] } is higher than {number_list[sort_index + 1]}") # O(1)
                higher_number = number_list[sort_index] # O(1)
                number_list[sort_index] = number_list[sort_index + 1] # O(1)
                number_list[sort_index + 1] = higher_number # O(1)
    return number_list # O(1)



def main():# O(n^2)
    number_list = [] # O(1)
    unsorted_list = request_numbers(number_list) # O(n)
    sorted_list =bubble_sort_list(unsorted_list) # O(n^2)
    print(sorted_list) # O(1)

if __name__ == "__main__":
    main() # O(n^2)