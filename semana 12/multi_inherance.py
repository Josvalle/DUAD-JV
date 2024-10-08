class Sum():
    def operation_sum(self,first_num,second_num):
        operation = first_num + second_num
        return print(f'The result of the sum is {operation}')
    

class Subtraction():
    def operation_subtraction(self,first_num,second_num):
        operation = first_num - second_num 
        return print(f'The result of the subtraction is {operation}')

class Multiplication():
    def operation_multiplication(self, first_num,second_num):
        operation = first_num * second_num
        return print(f'The result of the multiplication is {operation}') 

class Division():
    def operation_division(self,first_num,second_num):
        try:
            operation = first_num/second_num
            return print(f'The result of the division is {operation}')
        except ZeroDivisionError:
            print('Second number cannot be a "0"!')

class Calculator(Sum,Subtraction,Multiplication,Division):
    print('Welcome to the calculator'.center(20,'*'))


def loop_to_validate_input(selection,shape_parameter):
    if selection == '5':
        return
    else:
        while  True:
            try:
                shape_parameter = int(input(f'Please enter the value for {shape_parameter}: '))
                return shape_parameter
            except ValueError:
                print('The input enter is not a value number')


def main():
    calculator = Calculator()
    while True:
        selection = input('''
Please select the operation for the you would like to perform

1 = sum
2 = subtraction
3 = multiplication
4 = division
5 = exit
''')
        first_number = loop_to_validate_input(selection,'first_number')
        second_number = loop_to_validate_input(selection,'second_number')
        if selection == '1':
            calculator.operation_sum(first_number,second_number)
        elif selection == '2':
            calculator.operation_subtraction(first_number,second_number)
        elif selection == '3':
            calculator.operation_multiplication(first_number,second_number)
        elif selection == '4':
            calculator.operation_division(first_number,second_number)
        elif selection == '5':
            print('Thank you for using the calculator, bye! 👋')
            break
        else:
            print('Incorrect selection please try a valid option')

if __name__ == '__main__':
    main()