from sort_of_string import sort_of_the_string
import pytest 

def test_string_is_sort():
    #Arrange:
    string_test = "python-variable-function-computer-monitor"
    #Act
    result = sort_of_the_string(string_test)
    #Assert
    assert result == 'computer-function-monitor-python-variable'

def test_with_empty_string():
    #Arrange:
    string_test = ' '
    #Act
    result = sort_of_the_string(string_test)
    #Assert
    assert result == ' '

def test_with_invalid_input_integer():
    #Arrange:
    string_test = 9
    #Act & Assert
    with pytest.raises(ValueError):
        sort_of_the_string(string_test)