"""Homework 9.1."""

from contextlib import ExitStack
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(lst: List[Union[Path, str]]) -> Iterator:
    """Merge integer from infinite number of sorted sequences in files and return an iterator.

    Args:
        lst: paths

    Returns:
        The return value. Iterator object
    """
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in lst]
        fin = list(zip(*map(lambda x: map(int, list(x)), files)))
        return iter(sorted(j for i in fin for j in i))
