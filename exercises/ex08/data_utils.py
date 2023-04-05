"""EX08 Data Utils"""


__author__ = "730472095"


from csv import DictReader


DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table 
    for row in table: 
        #save every value under the key "header"
        result.append(row[header])
    return result 


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table 
    first_row: dict[str, str] = table[0]
    for key in first_row: 
        # for each key, make dictionary entry with all column values 
        result[key] = column_values(table, key)
    return result 


def head(table: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """Produce a new dictionary with just a certain number of rows for each column."""
    result: dict[str, list[str]] = {}
    # loop through each columns in the rows given in parameter
    for column in table:
        empty_list: list[str] = []
        for idx in range(row_num):
            empty_list.append(table[column][idx])
        result[column] = empty_list
    return result 


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new dictionary with only a specific set of columns from the original table."""
    result: dict[str, list[str]] = {}
    for name in names: 
        result[name] = table[name]
    return result 


def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new dictionary with two column based tables combinded."""
    result: dict[str, list[str]] = {}
    for column in dict_one:
        result[column] = dict_one[column]
    for column_two in dict_two:
        if column_two in result:
            result[column_two] += dict_two[column_two]
        else: 
            result[column_two] = dict_two[column_two]
    return result 


def count(count_list: list[str]) -> dict[str, int]:
    """A dictionary of how many times a value appeared in a list!"""
    result: dict[str, int] = dict()
    for item in count_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return (result) 