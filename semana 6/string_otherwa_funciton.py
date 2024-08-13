def flips_string():
    my_string = 'Luke I am your father'
    new_string = ' '
    for i in range(len(my_string) -1, -1,-1 ):
        new_string += my_string[i]
    return new_string

flip_new_string = flips_string()

print(flip_new_string)
