"""Homework 2.5."""

from typing import Any, List, Sequence


def find_seq_from_many_args(seq: Sequence, *args: Any, step: int = 1) -> List:
    """Find sequence from many arguments.

    Args:
        seq: iterable sequence
        *args: first element of sequence
                second element of sequence: optional
        step: step of elements in the output sequence: optional
            (if only one element of the sequence is passed, specify the step explicitly)

    Returns:
        The return value. ranged list of elements

    """
    number_arg1 = None
    number_arg2 = None
    for num, elem in enumerate(seq):
        if elem == args[0]:
            number_arg1 = num
        elif elem == args[1]:
            number_arg2 = num
    if len(args) == 3:
        step = args[2]
    return list(seq[number_arg1:number_arg2:step])


def custom_range(seq: Sequence, *args: Any, step: int = 1) -> List:
    """Accept any iterable of unique values and then behave as range function.

    Args:
        seq: iterable sequence
        *args: first element of sequence
                second element of sequence: optional
        step: step of elements in the output sequence: optional
            (if only one element of the sequence is passed, specify the step explicitly)

    Returns:
        The return value. ranged list of elements

    """
    if len(args) == 1:
        for num, elem in enumerate(seq):
            if elem == args[0]:
                return list(seq[:num:step])
        return None
    else:
        return find_seq_from_many_args(seq, *args)
