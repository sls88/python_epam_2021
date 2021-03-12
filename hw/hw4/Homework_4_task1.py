"""Homework 4.1."""


def read_magic_number(path: str) -> bool:
    """Check if number in an interval [1, 3).

    Args:
        path: file_path.txt

    Returns:
        The return value. True if number in an interval [1, 3), None if file is empty
    """
    try:
        with open(path) as file:
            for stri in file:
                return 1 <= int(stri) < 3
    except Exception:
        raise ValueError("The case of some error (condition of the task)")
