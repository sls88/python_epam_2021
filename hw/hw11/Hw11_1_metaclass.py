"""Homework 11.1."""
from typing import Dict, Tuple


class SimplifiedEnum(type):
    """Remove duplications in variables declarations.

     For example: __keys = ("XL", "L", "M", "S", "XS")
                    SomeClass.XL == "XL" -> True
    Args:
        type: builtins metaclass

    Returns:
        The return value. Create class with use metaclass
    """

    def __new__(cls, clsname: str, bases: Tuple, dct: Dict):
        """Create new class.

        Args:
            clsname: name of future class
            bases: parents of future class
            dct: attributes of future class
        """
        attrs = {}
        simple_enum_cls = super().__new__(cls, clsname, bases, dct)
        for name in dct[f"_{clsname}__keys"]:
            if name not in attrs:
                setattr(simple_enum_cls, name, name)
        return simple_enum_cls
