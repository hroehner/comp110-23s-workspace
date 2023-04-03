"""Dictionary Exercise 07!"""


__author__: "730472095"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Keys of a given dictionary should become the values and vice versa."""
    invert_dict: dict[str, str] = dict()
    for key in given_dict:
        if key in invert_dict:
            raise KeyError("There cannot be two keys with the same value!")
        else:
            invert_dict[given_dict[key]] = key
    return (invert_dict) 


def favorite_color(name_color_dict: dict[str, str]) -> str:
    """A str will be returned of the color that appears the most in the dictionary."""
    new_dict: dict[str, int] = dict()
    for color in name_color_dict: 
        if name_color_dict[color] in new_dict:
            new_dict[name_color_dict[color]] += 1
        else: 
            new_dict[name_color_dict[color]] = 1
    max_color: int = 0 
    color_name: str = ""
    for key in new_dict:
        current_color: int = int(new_dict[key]) 
        if (current_color > max_color):
            max_color = current_color
            color_name = key
    return (color_name)  


def count(count_list: list[str]) -> dict[str, int]:
    """A dictionary of how many times a value appeared in a list will be returned!"""
    new_dict: dict[str, int] = dict()
    for item in count_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return (new_dict) 