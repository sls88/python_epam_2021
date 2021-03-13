"""Homework 4.3."""
import sys


def my_precious_logger(text: str) -> str:
    """Receive a string and write it to stderr if line starts with "error" and to the stdout otherwise.

    Args:
        text: text

    Returns:
        The return value. text in stderr if line starts with "error", in stdout otherwise
    """
    if text.startswith("error"):
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
