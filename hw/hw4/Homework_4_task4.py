"""Homework 4.4."""

from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Take a number N as an input and returns N FizzBuzz numbers.

    Args:
        n: number N (must be < 1)

    Returns:
        The return value. N FizzBuzz numbers

    Detailed instruction how to run doctests:
     - Install Python 3.8 (https://www.python.org/downloads/)
     - Install pytest `pip install pytest`
     - Clone the repository <path your repository>
     - Checkout branch <your branch>
     - Open terminal
     - Follow the path to find the file with your programm
     - Call the command: python file_name.py
     - If the program was launched without errors, all the doctests passed,
       otherwise, the error message "Failed example: ..." and the tests that did not pass will be displayed
     - if you want to enable doctest via pytest: go to your project root and enter the command: pytest --doctest-modules

    >>> fizzbuzz(1)
    ['1']
    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    >>> fizzbuzz(0)
    Traceback (most recent call last):
        ...
    ValueError: Incorrect input
    >>> fizzbuzz(-5)
    Traceback (most recent call last):
        ...
    ValueError: Incorrect input
    >>> fizzbuzz(5.2)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    """
    if n < 1 or not n:
        raise ValueError("Incorrect input")
    else:
        seq = [str(i) for i in range(1, n + 1)]
    new_list = []
    for i in seq:
        if int(i) % 15 == 0:
            new_list.append("FizzBuzz")
        elif int(i) % 3 == 0:
            new_list.append("Fizz")
        elif int(i) % 5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(i)

    return new_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
