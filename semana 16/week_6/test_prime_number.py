from prime_numbers import return_of_primes
from prime_numbers import is_prime
import pytest

def test_if_number_on_list_are_prime():
    #arrange
    number_list = [2,4,3,5,6]
    #Act
    result = return_of_primes(number_list)
    #Assert
    assert result == [2,3,5]

def test_input_enter_is_not_integer():
    #Arrange:
    number = 'test'
    #Act & Arrange
    with pytest.raises(ValueError):
        is_prime(number)


def test_with_big_primes_numbers():
    #Arrange:
    number_list = [4444,2851,100,3331,500,2371,1000,5227]
    #Act
    result = return_of_primes(number_list)
    #Assert
    assert result == [2851,3331,2371,5227]
