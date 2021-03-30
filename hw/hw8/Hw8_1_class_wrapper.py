"""Homework 8.1."""
import csv
from keyword import iskeyword
from typing import List, NoReturn, Optional, Union


class KeyValueStorage:
    """Store keys and values in wrapper class, from file.

    Each entry is represented as key and value separated by = symbol
    Values can be strings or integer numbers. If a value can be treated both as a number and a string,
    it is treated as number. Class attributes (values) must be accessed via "." or via ['key_name']
    Args:
        path: file path (file.txt)
    """

    def __init__(self, path: str) -> None:
        self.path = path
        with open(path) as f:
            reader = csv.reader(f, delimiter="=")
            for row in reader:
                KeyValueStorage.__int_checker(row)
                KeyValueStorage.__key_checker(row[0])
                self.__dict__[row[0]] = row[1]

    @staticmethod
    def __int_checker(key_value_list: List[str]) -> Union[NoReturn, List[str]]:
        try:
            key_value_list[1] = int(key_value_list[1])
        except ValueError:
            pass
        return key_value_list

    @staticmethod
    def __key_checker(key: str) -> Union[NoReturn, str]:
        if iskeyword(key):
            raise KeyError("Invalid key name")
        return key

    def __getitem__(self, item: str) -> Union[NoReturn, str, int]:
        """Return value if the key exists and it is a string.

        example: instance['key_name']
        Args:
            item: key

        Returns:
            The return value. Value
        """
        if not isinstance(item, str):
            raise ValueError("The key should be string")
        if item in self.__dict__:
            return self.__dict__[item]
        else:
            raise ValueError("The key does not exist")

    def __setattr__(self, item: str, value: Union[str, int]) -> Optional[NoReturn]:
        """Set attribute value.

        Args:
            item: key
            value: value
        """
        try:
            self.__dict__[item] = value
        except Exception:
            raise ValueError("The value cannot be assigned to an attribute")

    def __getattr__(self, item: str) -> Union[NoReturn, str, int]:
        """Return value if the attribute exists.

        example: instance.attribute_name
        Args:
            item: attribute

        Returns:
            The return value. Value
        """
        if item in self.__dict__:
            return self.__dict__[item]
        raise AttributeError("The attribute does not exist")
