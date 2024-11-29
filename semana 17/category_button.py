import PySimpleGUI as sg



def category_window_add(category_list):
    layout = [  [sg.Text('Please enter the name of the new Category')],
                [sg.Text(f'Current Categories: {category_list}', enable_events=True) ],
                [sg.Input(key='Category_input', enable_events=True)],
                [sg.Button('Submit'),sg.Button('Exit')]]
    window = sg.Window("Add category", layout)
    
    check_list = [item.lower() for item in category_list]
    

    while True:
        event, values = window.read()
        lower_value = values['Category_input']
        lower_value =lower_value.lower()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Category_input' and values['Category_input'] and values['Category_input'][-1] not in ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            window['Category_input'].update(values['Category_input'][:-1])
        elif event == 'Submit' and lower_value in check_list:
            sg.popup('Category already exist!')
        elif event == 'Submit':
            new_category = values['Category_input']
            sg.popup('New Category add it to the list')
            category_list.append(new_category)
            break

    window.close()
