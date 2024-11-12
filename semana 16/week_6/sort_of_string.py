def split_of_string(my_string):
    split_string = my_string.split(sep='-',)
    return split_string


def sort_of_list(split_string):
    split_string.sort()
    return split_string

def convert_to_string(sort_string):
    new_string='-'.join(sort_string)
    return new_string

def sort_of_the_string(string):
    if type(string) == str:
        split_string =split_of_string(string)
        sort_string = sort_of_list(split_string)
        convert_string = convert_to_string(sort_string)
        return convert_string
    raise ValueError('The input enter is not a String')



def main():
    my_string = "python-variable-function-computer-monitor"
    convert_string = sort_of_the_string(my_string)
    print(convert_string)

if __name__ == "__main__":
    main()