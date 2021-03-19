"""TEST Homework 5.2."""

import functools

from hw.hw5.Hw5_t2_decorator import wrap


def print_result(func):
    @wrap(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function."""
        return func(*args, **kwargs)

    return wrapper


@print_result
def custom_sum(*args):
    """Sum any objects which have __add___."""
    return functools.reduce(lambda x, y: x + y, args)


def test_custom_sum_doc():
    actual_result = custom_sum.__doc__

    assert actual_result == "Sum any objects which have __add___."


def test_custom_sum_name():
    actual_result = custom_sum.__name__

    assert actual_result == "custom_sum"


def test_return_original_function():
    without_print = custom_sum.__original_func
    actual_result = without_print(1, 2, 3, 4)

    assert actual_result == 10
