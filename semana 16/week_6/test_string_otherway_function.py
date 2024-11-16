from string_otherwa_funciton import flips_string
import pytest 

def test_flip_of_string():
    #Arrange
    string = 'Hello'
    #Act
    result = flips_string(string)
    #Assert
    assert result == 'olleH'

def test_flip_of_string_with_spaces():
    #Arrange
    string = 'Luke I am your father'
    #Act
    result = flips_string(string)
    #Assert
    assert result == 'rehtaf ruoy ma I ekuL'

def test_using_incorrect_input():
    #Arrange
    incorrect_string = 2513
    #Act & Assert
    with pytest.raises(ValueError):
        flips_string(incorrect_string)