class Circle():
    def __init__(self):
        while True:
            try:
                self.radio = int(input('Please enter the radio of the circle: '))
                break
            except ValueError:
                print('That is not a number, Please enter a correct number! ')
    
    def area_circle(self):
        try:
            area = 3.14*(self.radio)**2
            return print(f'The area of the circle is  {area}')
        except AttributeError:
            print('The Value enter is not a number please enter again!')

def main():
    radio = Circle()
    radio.area_circle()

if __name__ == "__main__":
    main()



