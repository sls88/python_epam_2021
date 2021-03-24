"""Homework 7.1."""
from collections import deque
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Find the number of occurrences of element in the tree.

    Args:
        tree: tree
        element: element

    Returns:
        The return value. Number of occurrences of element
    """
    clean_list = []
    queue = deque()
    queue += [tree]
    while queue:
        elem = queue.popleft()
        if isinstance(elem, (str, bool, int)):
            clean_list.append(elem)
        elif isinstance(elem, dict):
            queue += list(elem.items())
        else:
            queue += list(elem)
    return sum(1 for i in clean_list if element == i)
