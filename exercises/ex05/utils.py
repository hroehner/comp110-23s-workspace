"""List Utility Functions!"""

__author__ = "730472095"


def only_evens(num_list: list[int]) -> list[int]:
    """Given a list of integers return the even elements."""
    even_list: list[int] = []
    for num in num_list:
        if num % 2 == 0: 
            even_list.append(num)
    return even_list 


def concat(list_one: list[int], list_two: list[int]) -> list[int]: 
    """A new list containing elements of the first list followed by all the elements in the second list."""
    new_list: list[int] = []
    for item in list_one: 
        new_list.append(item)
    for item in list_two: 
        new_list.append(item)
    return new_list


def sub(a_list: list[int], start: int, end: int): 
    """Creating a new list which is a subset of a given list between the start and end index."""
    additional_list: list[int] = []
    if start < 0: 
        start = 0 
    if end > len(a_list): 
        end = len(a_list) 
    if len(a_list) == 0: 
        return []
    if start >= len(a_list): 
        return []
    if end == 0: 
        return []
    while start < end: 
        additional_list.append(a_list[start])
        start += 1 
    return additional_list