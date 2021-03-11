"""Homework 3.3."""

from typing import Any, Callable, Dict, List, Sequence, Tuple


class Filter:
    """Helper filter class. Accepts a list of single-argument.

    Functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions: Tuple[Callable]):
        self.functions = functions

    def apply(self, data: Sequence[Any]) -> List[Any]:
        """Filter sequence."""
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords: Dict) -> Callable:
    """Generate filter object for specified keywords."""
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(el_of_seq: Any) -> Any:
            """Keyword filter."""
            if key not in el_of_seq:
                for k in keywords.keys():
                    return k in el_of_seq and k != key
            return el_of_seq[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)
