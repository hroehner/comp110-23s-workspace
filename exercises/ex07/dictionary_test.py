"""Dictionary Unit Tests for EX07!"""

__author__: "730472095"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_numerous_strings() -> None:
    """Testing invert function with a given dictionary of strings!"""
    test_dict: dict[str, str] = ({'george': 'roehner', 'maycie': 'rouse', 'charlie': 'dillon'})
    assert invert(test_dict) == ({'roehner': 'george', 'rouse': 'maycie', 'dillon': 'charlie'})


def test_empty_string() -> None: 
    """Testing invert function with two of the same key in a given dictionary!"""
    test_dict: dict[str, str] = ({})
    assert invert(test_dict) == {}


def test_two_pairs_of_strings() -> None: 
    """Testing two strings with invert function."""
    test_dict: dict[str, str] = ({'peanut': 'butter', 'strawberry': 'jam'})
    assert invert(test_dict) == {'butter': 'peanut', 'jam': 'strawberry'}


def test_numerous_colors() -> None: 
    """Testing numerous colors!"""
    test_dict: dict[str, str] = ({"helen": "pink", "grace": "yellow", "caroline": "blue", "jordan": "blue"})
    assert favorite_color(test_dict) == "blue"


def test_empty_dict() -> None: 
    """Testing empty dict."""
    test_dict: dict[str, str] = ({})
    assert favorite_color(test_dict) == ""


def test_same_value_for_colors() -> None: 
    """Testing favorite_colors that has the same value."""
    test_dict: dict[str, str] = ({"haley": "orange", "brian": "yellow", "stacy": "orange", "maya": "yellow"})
    assert favorite_color(test_dict) == "orange"


def test_numerous_strings_in_list() -> None: 
    """Testing numerous strings in a list and converting to a dicitonary."""
    test_count: list[int] = (["London", "Paris", "Bali", "London"])
    assert count(test_count) == {'London': 2, 'Paris': 1, 'Bali': 1}


def test_empty_list() -> None: 
    """Testing empty list!"""
    test_count: list[int] = ([])
    assert count(test_count) == {}


def test_list_same_count() -> None: 
    """Testing list to dictionary with keys all having the same value."""
    test_count: list[int] = (["eggs", "bacon", "pancakes"])
    assert count(test_count) == {'eggs': 1, 'bacon': 1, 'pancakes': 1}