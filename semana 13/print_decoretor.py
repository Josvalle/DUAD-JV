class person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    
    def display_user_information(self):
        return (f'Profile for: {self.name} {self.last_name} with the age of {self.age} has been create')

def print_parameters_return(func):
    def wrapper(person):
        print(f'These are the parameter of the function: {person.name}, {person.last_name}, {person.age}')
        result = func(person)
        print(f'The return of the function is: {result}')    
    return wrapper

@print_parameters_return
def user_input(person):
    print('creating profile...')
    return person.display_user_information()



def main():
    name = input('Please enter your name: ')
    last_name = input('Please enter your last name: ')
    age = input('Please enter your age: ')
    person_1 = person(name, last_name, age)
    user_input(person_1)


if __name__ == "__main__":
    main()