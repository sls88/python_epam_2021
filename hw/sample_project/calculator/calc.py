"""Homework 1.1.

"""


def check_power_of_2(a: int) -> bool:
    """Short description.

    Args:
        a: input positive number

    Returns: return True - is square of number
    False - not square of number

    """
    try:
        return not (bool(a & (a - 1)))
    except (TypeError, ValueError):
        print("Incorrect data type")
        return False
