"""Homework 2.1."""

import string
from collections import defaultdict
from typing import List


def filter_unicode_letters(let: str) -> bool:
    """Filter unicode letters.

    Args:
        let: letter

    Returns:
        The return value. True if is unicode letter

    """
    try:
        let.encode("ascii")
    except UnicodeEncodeError:
        return True
    return False


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. 10 longest words consisting from largest amount of unique symbols.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape").strip().split()
    clean_data = [word.strip(string.punctuation + "«»‹›’—") for word in data]
    clean_data.sort(key=lambda x: len(set(x)))
    return clean_data[len(data) - 10 :]


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document.

    If there are the same number of rare symbols in the document, any of them will be displayed.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. Rarest symbol for document.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape")
    dt = defaultdict(int)
    for let in list(data):
        dt[let] += 1
    return min(dt.items(), key=lambda item: int(item[1]))[0]


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. Amount of punctuation char.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape")
    return sum(1 for let in list(data) if let in (string.punctuation + "«»‹›’—"))


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. Amount of every non ascii char.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape")
    return sum(1 for let in list(data) if filter_unicode_letters(let))


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. Most common non ascii char for document.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape")
    dt = defaultdict(int)
    for let in list(data):
        if filter_unicode_letters(let):
            dt[let] += 1
    if dt:
        return max(dt.items(), key=lambda item: int(item[1]))[0]
    else:
        return "empty sequence"
