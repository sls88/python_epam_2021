"""Homework 9.3."""
import os
from os.path import isdir, join
from pathlib import Path
from typing import Callable, List, Optional


def lines_generator(root: Path, files: List, file_extension: str) -> str:
    """Generate lines from a file with a suitable extension.

    Args:
        root: directory path
        files: files in directory
        file_extension: file extension

    Returns:
        The return value. Line
    """
    for file in files:
        if file.endswith(file_extension):
            with open(join(root, file)) as f:
                for line in f:
                    yield line


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Сount lines / tokens in files with specified extension.

        count lines / tokens in files with specified extension
        count lines in all files with the specified extension, the specified directory,
        and all nested ones (recursively).
        If there is no tokenizer - read lines
        If the tokenizer function is defined - apply for token counting.
    Args:
        dir_path: directory path
        file_extension: file extension
        tokenizer: function for token counting

    Returns:
        The return value. Amount of lines or tokens (optional)
    """
    if not isdir(Path(dir_path)):
        raise FileNotFoundError("nonexistent directory")
    counter = 0
    for root, _, files in os.walk(Path(dir_path)):
        line = lines_generator(root, files, file_extension)
        if tokenizer:
            counter += sum(len(tokenizer(i)) for i in line)
        else:
            counter += sum(1 for i in line)
    return counter
