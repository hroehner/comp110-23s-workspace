"""EX04 - List Utiilty Exercise!"""

__author__ = "730472095"


def all(x: list[int], s: int) -> bool:
    """Finding to see if all ints found in a list match int in parameter!"""
    idx: int = 0 
    if len(x) == 0: 
        return False 
    while idx < len(x): 
        if x[idx] == s:
            idx += 1 
        else: 
            return False 
    return True 


def max(input: list[int]) -> int: 
    """Finding the maxium number in a list of ints."""
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    idx: int = 0 
    max_number: int = input[0]
    while idx < len(input): 
        current_int: int = input[idx]
        if (current_int > max_number): 
            max_number = current_int 
        idx += 1
    return max_number


def is_equal(y: list[int], z: list[int]) -> bool: 
    """Determining if the ints in one list, match the ints in another."""
    idx: int = 0 
    if len(y) == 0 and len(z) == 0: 
        return True
    if len(y) == 0 or len(z) == 0:
        return False 
    if len(y) != len(z): 
        return False 
    while idx < len(y):
        if y[idx] == z[idx]: 
            idx += 1
        else: 
            return False 
    return True 