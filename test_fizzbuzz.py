# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of 
# the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.

# CÓDIGO PRODUCCIÓN

def fizz_buzz(number):
    if number is None:
        raise NumberCannotBeNoneError
    if number % 3 == 0 and number % 5 == 0:
        return 'FIZZBUZZ'
    if number % 3 == 0:
        return 'FIZZ'
    if number % 5 == 0:
        return 'BUZZ'
    return number
    

import unittest
import pytest

# TESTS

class TestFizzBuzz(unittest.TestCase):
    # TEST 1
    def test_nine_returns_fizz(self):
        number = 9
        expected_result = 'FIZZ'

        result = fizz_buzz(number)

        assert result == expected_result
    
    # TEST 2
    def test_ten_returns_buzz(self):
        number = 10
        expected_result = 'BUZZ'

        result = fizz_buzz(number)

        assert result == expected_result

    # TEST 3
    def test_fifteen_returns_fizzbuzz(self):
        number = 15
        expected_result = 'FIZZBUZZ'

        result = fizz_buzz(number)

        assert result == expected_result

    # TEST 4
    def test_thirty_returns_fizzbuzz(self):
        number = 30
        expected_result = 'FIZZBUZZ'

        result = fizz_buzz(number)

        assert result == expected_result

    # TEST 5
    def test_nineteen_returns_nineteen(self):
        number = 19
        expected_result = 19

        result = fizz_buzz(number)  

        assert result == expected_result

    # TEST 6
    def test_number_is_none(self):
        number = None
        with pytest.raises(NumberCannotBeNoneError):
            assert fizz_buzz(number)

    # TEST 7
    def test_number_is_string(self):
        number = 't'
        with pytest.raises(TypeError):
            assert fizz_buzz(number)


class NumberCannotBeNoneError(Exception):
    pass


