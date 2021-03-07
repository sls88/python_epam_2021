"""Homework 2.1."""

import string
from collections import defaultdict
from typing import List


def clear_word_from_punctuation(word: str) -> str:
    """Сlear the word from punctuation characters around.

    if a double word is written with "-", the letter "-" will not be removed

    Args:
        word: word

    Returns:
        The return value. clear word

    """
    clear_word = word
    while True:
        for let in clear_word:
            if let in "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~«»‹›’—":
                clear_word = clear_word.replace(let, "")
            elif let == "-":
                clear_word = clear_word.strip("-")
        return clear_word


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. 10 longest words consisting from largest amount of unique symbols.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape").strip().split()
    for word_num, word in enumerate(data):
        data[word_num] = clear_word_from_punctuation(word)
    data.sort(key=lambda x: len(set(x)))
    return data[len(data) - 10 :]


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
    for stri in data:
        for let in stri:
            dt[let] += 1
    return min(dt.items(), key=lambda item: int(item[1]))[0]


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. Amount of punctuation char.

    """
    punctuation_count = 0
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape")
        for stri in data:
            for let in stri:
                if let in string.punctuation + "«»‹›’—":
                    punctuation_count += 1
        return punctuation_count


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char.

    Args:
        file_path: file path (file.txt)

    Returns:
        The return value. Amount of every non ascii char.

    """
    with open(file_path, "rb") as file:
        data = file.read().decode("unicode_escape")
    count_unicode_letters = 0
    for stri in data:
        for let in stri:
            try:
                let.encode("ascii")
            except UnicodeEncodeError:
                count_unicode_letters += 1
    return count_unicode_letters


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
    for stri in data:
        for let in stri:
            try:
                let.encode("ascii")
            except UnicodeEncodeError:
                dt[let] += 1
    if dt:
        return max(dt.items(), key=lambda item: int(item[1]))[0]
    else:
        return "empty sequence"
