def flips_string(my_string):
    if type(my_string) == str:
        new_string = ''
        for i in range(len(my_string) -1,-1,-1 ):
            new_string += my_string[i]
        return new_string
    raise ValueError('The input enter is not a string')

def main():
    my_string = 'Luke I am your father'
    flip_new_string = flips_string(my_string)
    print(flip_new_string)

main()
