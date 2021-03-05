"""Homework 1.3.

Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""


import logging
from typing import Tuple


def validate_number(str_number: str) -> int:
    """Validate number. Change type.

    Args:
        str_number: number

    Returns:
        The return values. number

    """
    if str_number == "":
        return None
    try:
        int(str_number)
    except ValueError:
        logging.error('The number has a "-" literal as a separator. Input data error.')
        return None
    return int(str_number)


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Find the minimum and maximum number in a text file.

        (it is forbidden to use the "-" as a separator)

    Args:
        file_name: sequence of lines from a text file containing integers

    Returns:
        The return values. (min(sequence), max(sequence))

    """
    with open(file_name) as file:
        data = file.readlines()
        data = " ".join(data)
        numbers_set = set()
        number = ""
        for lit in data:
            if "9" >= lit >= "0" or lit == "-":
                number += lit
            else:
                validate = validate_number(number)
                if validate is not None:
                    numbers_set.add(validate)
                number = ""
        return (min(numbers_set), max(numbers_set))
