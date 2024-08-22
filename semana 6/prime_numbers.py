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

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True





def return_of_primes(number_list):
    new_list = []
    for index, number in enumerate(number_list):
        if  is_prime(number):
            new_list.append(number)

    return new_list


def main():
    number_list = list_request_for_user()
    new_list = return_of_primes(number_list)
    print(new_list)

if __name__ == "__main__":
    main()