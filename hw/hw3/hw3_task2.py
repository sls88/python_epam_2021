"""Homework 3.2."""

import datetime
import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Any, Tuple


def slow_calculate(value):
    """Some weird voodoo magic calculations."""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def more_fast_slow_calculate(value: int) -> int:
    """Find a value like a function slow_calculate() more quickly.

    Args:
        value: number

    Returns:
        The return value. result
    """
    time.sleep(0.01)
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_more_fast_slow_calculate(number: int) -> int:
    """Find a sum values function slow_calculate() (more quickly).

    Args:
        number: range values from 0 to our number which we need to sum

    Returns:
        The return value. result    sum(0, 1, 2...number)
    """
    return sum(more_fast_slow_calculate(i) for i in range(number))


def fast_calculate(number: int) -> Tuple[Any]:
    """Find the sum of numbers of slow_calculate() function using multiprocessing method.

    Args:
        number: range values from 0 to our number which we need to sum

    Returns:
        The return values. result sum(0, 1, 2...number), datetime.timedelta() (program running time)
    """
    start_time = datetime.datetime.now()
    pool = Pool(processes=50)
    result = sum(pool.map(slow_calculate, (i for i in range(number))))
    end_time = datetime.datetime.now()
    return result, end_time - start_time
