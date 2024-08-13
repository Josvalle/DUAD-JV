def split_of_string(my_string):
    split_string = my_string.split(sep='-',)
    return split_string


def sort_of_list(split_string):
    split_string.sort()
    return split_string

def convert_to_string(sort_string):
    new_string='-'.join(sort_string)
    return new_string




def main():
    my_string = 'nissa-toyota-bmw-ferrari-honda-susuki-mercedez'
    split_string =split_of_string(my_string)
    sort_string = sort_of_list(split_string)
    convert_string = convert_to_string(sort_string)
    print(convert_string)

if __name__ == "__main__":
    main()