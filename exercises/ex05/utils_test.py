"""Unit test for Utils Exericse Five."""

__author__ = "730472095"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty_list() -> None:
    """Testing empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_many_num() -> None: 
    """Testing evens list with a given list."""
    test_list: list[int] = [1, 2, 3, 4]
    assert only_evens(test_list) == [2, 4]


def test_odd_num() -> None: 
    """Testing evens list with just odd numbers."""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == []


def test_two_list_with_same_length() -> None: 
    """Testing concat with two same length lists."""
    test_list_one: list[int] = ([1, 2, 3])
    test_list_two: list[int] = ([7, 8, 9])
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 7, 8, 9]


def test_two_list_with_different_lengths() -> None: 
    """Testing concat with two lists of different lengths."""
    test_list_one: list[int] = ([1, 2, 3, 4, 5, 6, 7, 8])
    test_list_two: list[int] = ([9, 10])
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_one_list() -> None: 
    """Testing concat with one list being empty."""
    test_list_one: list[int] = ([3, 6, 9])
    test_list_two: list[int] = ([])
    assert concat(test_list_one, test_list_two) == [3, 6, 9]


def test_sub_list() -> None: 
    """Testing sub with list of whole, postive numbers."""
    test_list: list[int] = ([4, 5, 8, 10])
    assert sub(test_list, 0, 2) == [4, 5]


def test_negative() -> None: 
    """Testing sub with a starting negative number."""
    test_list: list[int] = ([-10, 10, 20, 30, 40])
    assert sub(test_list, 0, 3) == [-10, 10, 20]


def test_length_of_list_is_zero() -> None: 
    """Testing sub list with a length of zero."""
    test_list: list[int] = ([])
    assert sub(test_list, 0, 0) == []