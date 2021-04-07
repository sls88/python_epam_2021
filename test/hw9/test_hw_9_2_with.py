"""TEST Homework 9.2."""
import pytest

from hw.hw9.Homework_9_2_with import Supressor, supressor


def test_supressor_gen():
    with supressor(IndexError):
        [][2]


def test_supressor_gen_neg():
    with pytest.raises(IndexError):
        with supressor(KeyError):
            [][2]


def test_supressor_class():
    with Supressor(IndexError):
        [][2]


def test_supressor_class_neg():
    with pytest.raises(IndexError):
        with Supressor(KeyError):
            [][2]
