import PySimpleGUI as sg
from os.path import exists
from data import import_csv_file
from data import export_csv
from data import obtain_current_balance
from category_button import category_window_add
from spent_button import spent_button
from income_button import income_button

def principal_window(table_list, category_list):
    balance = ''
    headings = ['Description', 'Category', 'Type', 'Amount','Notes' ]
    layout = [[sg.Text("Hi Welcome to your Finance board")],[
                sg.Table(values=table_list, headings=headings,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='center',
                                    num_rows=10,
                                    key='-TABLE-')],[
                                        sg.Text(f'Balance: {balance}', key='balance'), sg.Button('Check Balance', key='balance_bt')
                                    ],
                [sg.Button('Add new category', key="category_bt"),sg.Button('Spent', key="spent_bt"),sg.Button('Income', key='income_bt')],
                [sg.Button('Exit')]]
    window = sg.Window("Personal Finance", layout)

    while True:
        
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == "category_bt":
            category_window_add(category_list)
        elif event == "spent_bt":
            if not category_list:
                sg.PopupError('Please add a category first')
            else:
                spent_button(table_list,category_list)
                window['-TABLE-'].update(table_list)
                export_csv(table_list)
        elif event == 'income_bt':
            if not category_list:
                sg.PopupError('Please add a category first')
            else:
                income_button(table_list,category_list)
                window['-TABLE-'].update(table_list)
                export_csv(table_list)
        elif event == 'balance_bt':
            balance = obtain_current_balance(table_list,balance)
            window['balance'].update(balance)



    window.close()

def main():
    table_list = []
    category_list = []
    if exists('info.csv'):
        table_list, category_list = import_csv_file('info.csv',table_list,category_list) 
    principal_window(table_list, category_list)

if __name__ == "__main__":
    main()