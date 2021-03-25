"""Homework 6.1."""
from typing import Any, Dict


def instances_counter(cls: Any) -> Any:
    """Add 2 methods to the class.

    get_created_instances - Returns the number of created class instances
    reset_instances_counter - reset the instance counter,returns the value before reset

    Args:
        cls: any class

    Returns:
        The return value. A class with two added methods.
    """
    cls.count = 0

    def __new__(class_name: Any, *args: Any, **kwargs: Dict[Any, Any]) -> Any:
        cls.count += 1
        return super(cls, class_name).__new__(class_name, *args, **kwargs)

    @classmethod
    def get_created_instances(cls: Any) -> int:
        """Return the number of created class instances."""
        return cls.count

    @classmethod
    def reset_instances_counter(cls: Any) -> int:
        """Reset the instance counter,returns the value before reset."""
        till_reset = cls.count
        cls.count = 0
        return till_reset

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls
