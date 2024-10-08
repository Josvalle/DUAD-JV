from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radio):
        self.radio = radio
    
    def calculate_perimeter(self,radio):
        perimeter = radio *2 * 3.14
        return print(f'The perimeter of the circle is: {perimeter}')
    

    def calculate_area(self,radio):
        area = 3.14*(radio)**2
        return print(f'The area of the circle is: {area}')

class Square(Shape):
    def __init__(self,side):
        self.side = side 
    
    def calculate_perimeter(self,side):
        perimeter = side + side + side + side
        return print(f'The perimeter of the square is: {perimeter}')
    
    def calculate_area(self,side):
        area = side * side
        return print(f'The area of the square is: {area}')

class Rectangle(Shape):
    def __init__(self,length, width ):
        self. length = length
        self.width = width
    
    def calculate_perimeter(self,length, width):
        perimeter = (2*length)+(2*width)
        return print(f'The perimeter of the rectangle is: {perimeter}')
    
    def calculate_area(self,length, width):
        area = length * width
        return print(f'The Area of the rectangle is: {area}')


def loop_to_validate_input(shape_parameter):
    while  True:
        try:
            shape_parameter = int(input(f'Please enter the value for {shape_parameter}: '))
            return shape_parameter
        except ValueError:
            print('The input enter is not a value number')


def circle_shape_operations():
    radio = loop_to_validate_input('radio')
    circle = Circle(radio)
    while True:
        operation_selection = input('Please select an operation: 1 = perimeter | 2 = area: ')
        
        if operation_selection == '1':
            operation_result = circle.calculate_perimeter(radio)
            return operation_result
        elif operation_selection == '2':
            operation_result = circle.calculate_area(radio)
            return operation_result
        else:
            print('Error: please select a valid operation')


def square_shape_operations():
    side = loop_to_validate_input('side')
    square = Square(side)
    while True:
        operation_selection = input('Please select an operation: 1 = perimeter | 2 = area: ')
        
        if operation_selection == '1':
            operation_result = square.calculate_perimeter(side)
            return operation_result
        elif operation_selection == '2':
            operation_result = square.calculate_area(side)
            return operation_result
        else:
            print('Error: please select a valid operation')


def rectangle_shape_operations():
    length = loop_to_validate_input('length')
    width = loop_to_validate_input('width')
    rectangle = Rectangle(length,width)
    while True:
        operation_selection = input('Please select an operation: 1 = perimeter | 2 = area: ')
        
        if operation_selection == '1':
            operation_result = rectangle.calculate_perimeter(length,width)
            return operation_result
        elif operation_selection == '2':
            operation_result = rectangle.calculate_area(length,width)
            return operation_result
        else:
            print('Error: please select a valid operation')





def main():
    while True:
        shape_selection = input('''
    Please select the Shape you want to calculate:

    1 = Circle
    2 = Square
    3 = Rectangle
    4 = Exit
    
    Your selection: 
    ''')
        
        if shape_selection == '1':
            circle_shape_operations()
        elif shape_selection =='2':
            square_shape_operations()
        elif shape_selection == '3':
            rectangle_shape_operations()
        elif shape_selection == '4':
            print('Thank you!')
            break
        else:
            print('Incorrect selection please try again!')

if __name__ == '__main__':
    main()


