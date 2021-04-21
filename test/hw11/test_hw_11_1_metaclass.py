"""TEST Homework 11.1."""

from hw.hw11.Hw11_1_metaclass import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_colors_enum():
    assert ColorsEnum.RED == "RED"


def test_sizes_enum():
    assert SizesEnum.XL == "XL"
