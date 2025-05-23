from orm import User,Cars,UserAddress, check_if_table_exist




def options_for_table():
    while True:
        table = input('''
        Menu:
            1 - User
            2 - Cars
            3 - Address

        ''')

        if table == 1:
            table_action = User()

            try:
                action = int(input('''
                1 - create new user
                2 - Modified user
                3 - detele user'''))
                
                if action == 1:
                    first_name = input('Please enter the first name: ')
                    last_name = input('Please enter the last name: ')
                    user_email = input('Please enter the email of the user: ')
                    table_action.create_new_user(first_name,last_name,user_email)
                elif action == 2:
                    column = input('Please enter the column you want to modified: ')
                    user_email = input('please enter the email of the user you want to modified: ')
                    new_value = input('Please enter the new value for the user: ')
                    table_action.modify_user(column,user_email,new_value)
                elif action == 3:
                    user_email = input('please enter the email of the user you want to delete: ')
                    table_action.delete_user(user_email)
                else:
                    print('Incorrect selection please select a valid option!!!')
            except Exception as ex:
                print(ex)
        elif table == 2:
            table_action = Cars()
            try:
                action = int(input('''
                1 - create new car
                2 - Modified car
                3 - detele car
                4 - end program'''))
                
                if action == 1:
                    plate = input('Please plate for the car: (only 6 values)')
                    option = input('Do you want to add a user: (yes/no)')
                    if option == 'yes' or option == 'y':
                        user = int(input('please enter the id of the user'))
                        table_action.create_new_car(user, plate)
                    table_action.create_new_car(plate)
                elif action == 2:
                    column = input('Please enter the column you want to modified: ')
                    plate = input('please enter the plate for the car you want to modified: ')
                    new_value = input('Please enter the new value for the car: ')
                    table_action.modify_car(column,plate,new_value)
                elif action == 3:
                    plate = input('please enter the plate for the car you want to delete: ')
                    table_action.delete_car(plate)
                else:
                    print('Incorrect selection please select a valid option!!!')
            except Exception as ex:
                print(ex)
        elif table == 3:
            table_action = UserAddress()
            try:
                action = int(input('''
                1 - create new Address
                2 - Modified Address
                3 - detele Address'''))
                
                if action == 1:
                    user_id = int(input('Please plate for the car: (only 6 values)'))
                    address = input('please enter the address of the user')
                    
                    table_action.create_new_address(user_id,address)
                elif action == 2:
                    column = input('Please enter the column you want to modified: ')
                    user_id = input('please enter the user id for the address  you want to modified: ')
                    new_value = input('Please enter the new value for the address: ')
                    table_action.modify_address(column,user_id,new_value)
                elif action == 3:
                    user_id = input('please enter the user id for the address you want to delete: ')
                    table_action.delete_address(user_id)
                else:
                    print('Incorrect selection please select a valid option!!!')
            except Exception as ex:
                print(ex)
        elif table == 4:
            break
        else:
            print('Please select a valid option!')


def main():
    check_if_table_exist()
    options_for_table()


if __name__ == "__main__":
    main()