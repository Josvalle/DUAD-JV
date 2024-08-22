my_list=[1,2,3,4,5,6,7,8,9,10,11,12]


for i,j in enumerate(my_list):
    if j % 2 != 0:
        my_list.remove(j)

print(my_list)