import csv

def user_get_info():

        keys_list = ['name','gender','developer','classification']
        value_list = []

        name = input('Please enter the name of the game: ')
        gender = input('Please enter the gender of the game: ')
        developer = input('Please enter the developer of the game: ')
        classification = input('Please enter the classification of the game: ')

        value_list.append(name)
        value_list.append(gender)
        value_list.append(developer)
        value_list.append(classification)

        new_dictionary = dict(zip(keys_list,value_list))
        
    
        return new_dictionary

def user_add_inform_list(games_information):

    exit = 'y'
    while exit == 'y':
        games_info = user_get_info()
        games_information.append(games_info)
        exit = input('Do you want to add a new games information? (y/n)')
    
    
    return games_information


def write_csv_file(file_path,games_information,games_headers):
    with open(file_path, 'w', encoding='utf=8') as file:
        writer = csv.DictWriter(file, fieldnames=games_headers)
        writer.writeheader()
        writer.writerows(games_information)


def main():
    games_information = [
    {
        'name' : 'Grand Theft Auto IV',
        'gender' : 'Action',
        'developer': 'Rockstar Games',
        'classification': 'M',
    }
]
    
    games_headers = (
        'name',
        'gender',
        'developer',
        'classification'
    )
    user_add_inform_list(games_information)
    write_csv_file('semana 8/games.csv', games_information,games_headers)


if __name__ == "__main__":
    main()




