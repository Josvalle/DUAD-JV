class BankAccount:
    balance = 1000

    def add_money(self, amount):
        self.balance += amount

    def remove_money(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
    
#pregunta por que si en los metodos de Bankaccount tengo que poner el self?
    def bank_operation(self,operation_choose,amount):
        if operation_choose == '1':
            BankAccount.add_money(self,amount)
        elif operation_choose == '2':
            if (self.balance - amount) > self.min_balance:
                BankAccount.remove_money(self,amount)
            else:
                print('Error de amount you want to withdraw is higher the min_balance')


def main():
    my_account = SavingsAccount(100)
    
    while True:
        print(f'''
Welcome to your Bank you current balance is {my_account.balance}
''')
        operation_choose = input('''What operation you would like to perform today:

1: Add money to the account 
2: Withdraw from your account
3: Leave the program 

Your option: 
''')
        while True:
                try:
                    amount = int(input('Please enter the amount of money you would like to add or withdraw from your account: '))
                    break
                except ValueError:
                    print('Please enter a numerical amount')

        if operation_choose == '1':
            my_account.bank_operation(operation_choose,amount)
        elif operation_choose == '2':
            my_account.bank_operation(operation_choose,amount)
        elif operation_choose == '3':
            print('Thank you have a good day')
            break
        else:
            print('ERROR: option selected is not a valid option. Please select a valid one!')

if __name__ == '__main__':
    main()