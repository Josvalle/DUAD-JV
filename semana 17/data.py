import csv

def convert_dict_to_list(list_of_dicts):
    new_list_of_list = []
    for item in list_of_dicts:
        description = item['Description']
        category =item['Category']
        type = item['Type']
        amount = int(item['Amount'])
        note = item['Notes']
        
        new_list_of_list.append([description,category,type,amount,note])
    return new_list_of_list

def convert_list_to_dict(table_list):
    list_of_dicts = []
    for item in table_list:
        description = item[0]
        category = item[1]
        type = item[2]
        amount = item[3]
        note = item[4]
        list_of_dicts.append({
            'Description' : description,
            'Category' : category,
            'Type' : type,
            'Amount' : amount,
            'Notes' : note

        })
    return list_of_dicts

def create_csv_file(file_path,dict_list,table_headers):
    with open(file_path, 'w', encoding='utf=8') as file:
        writer = csv.DictWriter(file, fieldnames=table_headers)
        writer.writeheader()
        writer.writerows(dict_list)

def export_csv(table_list):
    
    table_headers = (
        'Description',
        'Category',
        'Type',
        'Amount',
        'Notes',
    )
    convert_table_list = convert_list_to_dict(table_list)
    create_csv_file('info.csv',convert_table_list, table_headers)


def obtain_category_for_import(table_list, category_list):
    for category in table_list:
        new_item = category[1]
        category_list.append(new_item)
        category_list = list(dict.fromkeys(category_list))
    return category_list

def import_csv_file(file_path,table_list,category_list):
    
    try:
        
        with open(file_path,'r') as file:
            reader_of_file = csv.DictReader(file)
            list_of_dicts = list(reader_of_file)
        
        convert_table_list = convert_dict_to_list(list_of_dicts)
        table_list.extend(convert_table_list)
        new_category_list = obtain_category_for_import(table_list,category_list)
        return table_list, new_category_list
    except FileNotFoundError:
        print('There is not file no import yet, please first export a file')

def obtain_current_balance(table_list,balance):
    amount = 0
    balance = 0
    for item in table_list:
        amount = item[3]
        balance += amount
    return (f'Balance: {balance}')