"""Homework 4.2."""
import requests
from requests import RequestException


def count_dots_on_i(url: str) -> int:
    """Count how many letters `i` are present in the HTML by this URL.

    Args:
        url: URL

    Returns:
        The return value. Amount of letters `i`
    """
    try:
        res = requests.get(url)
    except RequestException:
        raise ValueError("Unreachable URL {}".format(url))
    return sum(1 for i in list(res.text) if i == "i")
