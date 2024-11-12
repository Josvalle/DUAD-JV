from bubble_sort_pyt import bubble_sort_list
import pytest
from random import randint

def test_bubble_sort_with_small_list():
    #arrange
    number_list = [6,2,1,7]
    #Act
    result = bubble_sort_list(number_list)
    #Assert
    assert result == [1,2,6,7]

def test_bubble_sort_with_list_for_hundred_items():
    #arrange
    number_list = [randint(1,100) for i in range(100)]
    sorted_list = sorted(number_list)
    #Act
    result = bubble_sort_list(number_list)
    #Assert
    assert result == sorted_list

def test_bubble_sort_with_list_empty():
    #arrange
    number_list = []
    #Act
    result = bubble_sort_list(number_list)
    #Assert
    assert result == []

def test_try_with_incorrect_input():
    #arrange
    number_list = 'hi'
    #Act & Assert
    with pytest.raises(ValueError):
        bubble_sort_list(number_list)

