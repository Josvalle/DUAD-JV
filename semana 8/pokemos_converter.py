import json


def open_jason():
    with open('semana 8/pokemons.json') as file:
        convert_python = json.load(file)
        
        return convert_python


def get_pokemon_info():
    name = input('Please enter the pokemon name: ')
    type = input('Please enter the type for the pokemon: ')
    hp = input('Please enter the HP for the pokemon: ')
    attack = input('Please enter the Attack  for the pokemon: ')
    defense = input('Please enter the defense for the pokemon: ')
    sp_attack = input('Please enter the SP. Attack for the pokemon: ')
    sp_defense = input('Please enter the SP. Defense for the pokemon: ')
    speed = input('Please enter the speed for the pokemon: ')

    return {
    "name": {
        "english": name
    },
    "type": [
        type
    ],
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
    }


def add_new_pokemon_to_list(convert_python):
    exit = 'y'
    while exit == 'y':
        new_pokemon  = get_pokemon_info()
        convert_python.append(new_pokemon)
        exit = input('Do you want to add a new games information? (y/n)')
    
    return convert_python


def write_new_json(convert_python, new_file_json):
    convert_json = json.dumps(convert_python)
    with open(new_file_json, 'w') as file:
        file.write(convert_json)


def main():
    convert_python = open_jason()
    add_new_pokemon_to_list(convert_python)
    write_new_json(convert_python, 'semana 8/new_pokemons.json')


if __name__ == "__main__":
    main()














