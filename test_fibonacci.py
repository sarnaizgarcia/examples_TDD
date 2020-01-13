## CÓDIGO PRODUCCIÓN

def my_fibonacci(index):
    
    if index is None:
        raise IndexCannotBeNoneError
    if index == 0 or index == 1:
        return index
    if index < 0:
        return None
    return my_fibonacci(index - 1) + my_fibonacci(index - 2)
    

import unittest
import pytest

## CÓDIGO DE TESTS

class TestFibonacci(unittest.TestCase):
    # TEST 1
    def test_index_zero_return_zero(self):
        index = 0
        expected_result = 0

        result = my_fibonacci(index)

        assert result == expected_result

    # TEST 2
    def test_index_one_return_one(self):
        index = 1
        expected_result = 1

        result = my_fibonacci(index)

        assert result == expected_result

    # TEST 3
    def test_index_two_return_one(self):
        index = 2
        expected_result = 1

        result = my_fibonacci(index)

        assert result == expected_result

    # TEST 4
    def test_index_three_return_two(self):
        index = 3
        expected_result = 2

        result = my_fibonacci(index)

        assert result == expected_result

    # TEST 5
    def test_index_four_return_three(self):
        index = 4
        expected_result = 3

        result = my_fibonacci(index)

        assert result == expected_result

    # TEST 6
    def test_index_six_return_eight(self):
        index = 6
        expected_result = 8

        result = my_fibonacci(index)

        assert result == expected_result
    
    # TEST 7
    def test_index_ten_return_fiftyfive(self):
        index = 10
        expected_result = 55

        result = my_fibonacci(index)

        assert result == expected_result

    # TEST 8
    def test_index_is_letter(self):
        index = 't'
        
        with pytest.raises(TypeError):
            assert my_fibonacci(index)
    
    # TEST 9
    def test_index_is_negative(self):
        index = -8
        expected_result = None

        result = my_fibonacci(index)

        assert result == expected_result
    
    # TEST 10
    def test_index_none_raise_error(self):
        index = None
        with pytest.raises(IndexCannotBeNoneError):
            assert my_fibonacci(index)


class IndexCannotBeNoneError(Exception):
    pass