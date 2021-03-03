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


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Find the minimum and maximum number in a text file.

        (it is forbidden to use the "-" as a separator)

    Args:
        file_name: sequence of lines from a text file containing integers

    Returns:
        The return values. (min(sequence), max(sequence))

    """
    with open(file_name) as fi:
        numbers_set = set()
        number = ""
        for line in fi:
            for lit in line:
                if "9" >= lit >= "0" or lit == "-":
                    number += lit
                else:
                    if number:
                        try:
                            numbers_set.add(int(number))
                        except ValueError:
                            logging.error(
                                'The number has a "-" literal as a separator. Input data error.'
                            )
                        number = ""
        return (min(numbers_set), max(numbers_set))
