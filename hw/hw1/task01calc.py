"""Homework 1.1."""

import logging


def check_power_of_2(a: int) -> bool:
    """Check if a number is an integer square logarithm.

    Args:
        a: positive number (not 0)

    Returns:
       The return value. True if a number is an integer square logarithm

    """
    if a == 0:
        logging.error("Incorrect number")
        return False
    return not (bool(a & (a - 1)))
