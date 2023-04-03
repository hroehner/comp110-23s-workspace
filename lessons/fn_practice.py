"""Example functions to learn definition and calling syntax."""

def my_max(num1: int, num2: int) -> int:
    """Returns the maximum value out two numbers"""
    if num1 >= num2: 
        return num1 + 0
    else:  #number1 < number 2
        return num2

max_number: int = my_max(1,12)
other_max_number: int = my_max(13,3)
print(other_max_number)