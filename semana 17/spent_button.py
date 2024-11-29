import PySimpleGUI as sg
from category_button import category_window_add

def spent_button(table_list,category_list):
    layout = [
        [sg.Text('Please enter the Description: '), sg.Input(key='description_input', enable_events=True)],
        [sg.Text('Please enter the select a Category: '), sg.OptionMenu(category_list, default_value=category_list[0], key='category_menu')],
        [sg.Text('Please enter the Amount: '), sg.Input(key='amount_input', enable_events=True)],
        [sg.Text('Please enter the Notes: '), sg.Input(key='notes_input', enable_events=True)],
        [sg.Button('Submit spent', key='submit_spt'), sg.Button('Not seeing your category?', key='crt_category')],
        [sg.Button('Exit')]]
    window = sg.Window("Add Spent", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'description_input' and values['description_input'] and values['description_input'][-1] not in ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            window['description_input'].update(values['description_input'][:-1])
        elif event == 'notes_input' and values['notes_input'] and values['notes_input'][-1] not in ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '):
            window['notes_input'].update(values['notes_input'][:-1])
        elif event == 'amount_input' and values['amount_input'] and values['amount_input'][-1] not in ('0123456789'):
            window['amount_input'].update(values['amount_input'][:-1])
        elif event == 'crt_category':
            window.close()
            category_window_add(category_list)
            
        elif event == 'submit_spt':
            if not values['description_input']:
                sg.PopupError('The Description cannot be empty.')
            elif not values['amount_input']:
                sg.PopupError('The Amount cannot be empty.')
            elif not values['notes_input']:
                sg.PopupError('The Notes cannot be empty.')
            else:
                new_add = [values['description_input'],values['category_menu'],'Expense',- + int(values['amount_input']),values['notes_input']]
                table_list.append(new_add)
                sg.Popup('Submission complete!!')
                break

    window.close()

