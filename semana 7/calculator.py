def sum(current_number,user_number):
    result = current_number + user_number
    print(result)
    return result


def subtraction(current_number,user_number):
    result = current_number - user_number
    return result


def division(current_number,user_number):
    try:
        result = current_number/user_number
        return result
    except ZeroDivisionError as ex:
        print(f'Unable to perform division: {ex}')


def multiplication(current_number,user_number):
    
    if current_number == 0:
        current_number = 1
    
    result = current_number*user_number
    return result


def user_selection_check(operations):

    try:
        while True:
                operation_selected = input('''
Please select one of the option
1 = Sum
2 = Subtraction
3 = Division
4 = multiplication
5 = Erase result 

Your option: ''')
                if operation_selected in operations:
                    return operation_selected
                else:
                    print('Incorrect selection, try again')

    except ValueError:
        print('The option selected is not on the list, try again')
    except IndexError:
        print('The option selected is not on the list, try again')


def operations_result(operation_selected,current_number):
    if operation_selected == '5':
            final_return = 0
            return final_return
            
    try:
        user_number = input('Please enter the number for the operation: ')
        user_number = int(user_number)
        if operation_selected == '1':
            final_return = sum(current_number,user_number)
        elif operation_selected == '2':
            final_return = subtraction(current_number,user_number)
        elif operation_selected == '3':
            final_return = division(current_number,user_number)
        elif operation_selected == '4':
            final_return = multiplication(current_number,user_number)
        else:
            final_return == current_number
        
        
        return final_return
    except ValueError as ex:
        print(f'The character enter is not a number: {ex}')


def main():
    current_number = 0
    operations = ['1','2','3','4','5']
    exit = 'y'
    try:
        while exit == 'y':
            print(f'Current number = {current_number}')
            operation_selected = user_selection_check(operations)
            results = operations_result(operation_selected,current_number)
            current_number = results
            print(f'Current number = {results}')

            while True:
                exit = input('Do you want to continue with the operation (y/n): ')
                
                if exit == 'n' or exit == 'y':
                    break
                else:
                    print('The option enter is not valid, please try again')
    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')



if __name__ == "__main__":
    main()


