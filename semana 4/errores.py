test_string = "test"
test_integer = 27
test_list = [23, "hello", test_string, False]
second_list = ['operand', True, test_integer]
test_float = 23.56

sum_string = test_string + " string" 
#sum_string_int = test_string + test_integer       #TypeError: can only concatenate str (not "int") to str
#sum_string_int_1 = test_integer + test_string     #TypeError: unsupported operand type(s) for +: 'int' and 'str'
sum_list = test_list + second_list 
#sum_string_list = test_string + test_list          #TypeError: can only concatenate str (not "list") to str
sum_float_int = test_float + test_integer         
sum_bool = False + True

print(sum_string)
print(sum_list)
print(sum_float_int)
print(sum_bool)



