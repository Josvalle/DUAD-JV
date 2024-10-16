from datetime import date

class User:
    date_of_birth : int
    name : str
    last_name : str

    def __init__(self,date_of_birth,name,last_name):
        self.date_of_birth = date_of_birth
        self.name = name
        self.last_name = last_name

    @property
    def age_checker(self):
        today = date.today()
        day,month,year = map(int, self.date_of_birth.split("-"))
        age = today.year - year - ((today.month, today.day) < (month,day))
        if age < 18:
            raise ValueError('User enter is under 18!!')
        else:
            return 'You can enter'

def main():
    name = input('Please enter you name: ')
    last_name = input('Please enter your last name: ')
    date_of_birth = input('Please enter your date of birth on the following format (day-month-year): ')
    user = User(date_of_birth, name,last_name)
    print(f'The user {user.name}:  {user.age_checker}')

if __name__ == "__main__":
    main()
