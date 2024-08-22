
global_variable = 6

def access_global():
    global_variable = 7
    print(global_variable)


def inside_variable():
    name='Jose'
    return name

access_inside = inside_variable()


access_global()
print(access_inside)
