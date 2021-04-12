"""Homework 9.1."""

import logging
from pathlib import Path
from types import TracebackType
from typing import Iterator, List, NoReturn, Union


class Line:
    """Give information about the next value and return if necessary.

        Iterator for each file received
    Args:
        file: open file

    Returns:
        The return value. Next value
    """

    def __init__(self, file: "_io.TextIOWrapper"):
        self.file = file
        x = self.file.tell()
        self.next_el = int(self.file.readline())
        self.file.seek(x)

    def __iter__(self) -> "Line":
        """Return an iterator instance for each file."""
        return self

    def __next__(self) -> Union[int, NoReturn]:
        """Return next value."""
        n = self.file.readline()
        if n:
            x = self.file.tell()
            next_str = self.file.readline()
            self.file.seek(x)
            self.next_el = int(next_str) if next_str else float("inf")
            return int(n)
        raise StopIteration

    def __lt__(self, other: int) -> bool:
        """Find the min() function of self.next_el.

        Args:
            other: other element to compare

        Returns:
            The return value. True if other element is more
        """
        return self.next_el < other.next_el


class Iterator:
    """Select the lowest-valued iterator and iterate.

    Args:
        files: List of open files

    Returns:
        The return value. Next minimal value
    """

    def __init__(self, files: List["_io.TextIOWrapper"]) -> None:
        self.files = files
        self.lst = [Line(i) for i in self.files]
        self.el = {i.next_el for i in self.lst}

    def __iter__(self) -> Iterator:
        """Return an iterator instance."""
        return self

    def __next__(self) -> Union[int, NoReturn]:
        """Return next lowest count."""
        if self.el is not {float("inf")}:
            for i in min(self.lst):
                return i
        raise StopIteration


class merge_sorted_files:
    """Open all transferred files. After work - close.

    Args:
        lst: List of paths

    Returns:
        The return value. Iterator
    """

    def __init__(self, lst: List[Union[Path, str]]):
        self.lst = lst

    def __enter__(self) -> Iterator:
        """Open all transferred files."""
        self.file_open_list = [open(Path(i)) for i in self.lst]
        return Iterator(self.file_open_list)

    def __exit__(
        self, exc_type: Exception, exc_val: Exception, exc_tb: TracebackType
    ) -> None:
        """Close all files. If exception occure - output in log."""
        for i in self.file_open_list:
            try:
                i.close()
            finally:
                if exc_val:
                    logging.error(exc_val)
                continue
