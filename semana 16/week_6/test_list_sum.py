from list_sum import sum_of_list_number

def test_sum_list_small_number():
    #arrange
    number_list = [6,2,1,7]
    #Act
    result = sum_of_list_number(number_list)
    #Assert
    assert result == 16


def test_sum_list_big_number():
    #arrange
    number_list = [6000,2500,1461,777]
    #Act
    result = sum_of_list_number(number_list)
    #Assert
    assert result == 10738


def test_sum_list_with_20_entries():
    #arrange
    number_list = [1,2,3,4,5,6,7,8,9,10,222,45,35,874,30,22,77,98,1000,79]
    #Act
    result = sum_of_list_number(number_list)
    #Assert
    assert result == 2537