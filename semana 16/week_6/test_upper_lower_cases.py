from upper_lower_cases import count_upper_lower_cases

def test_count_using_simple_string():
    #Arrange
    string = 'Hello'
    #Act
    upper_result, lower_result = count_upper_lower_cases(string)
    #Assert
    assert upper_result == 1 and lower_result ==4

def test_count_using_string_with_spaces():
    #Arrange
    string = 'Hello How Are You'
    #Act
    upper_result, lower_result = count_upper_lower_cases(string)
    #Assert
    assert upper_result == 4 and lower_result  == 10


def test_count_using_empty_string():
    #Arrange
    string = ''
    #Act
    upper_result, lower_result = count_upper_lower_cases(string)
    #Assert
    assert upper_result == 0 and lower_result == 0