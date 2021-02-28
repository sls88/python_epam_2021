"""TEST Homework 1.1.

"""
import pytest
from epam_python_2021.hw.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (65536, True),
        (12, False),
        ("c", False),
        (None, False),
        (0, True),
        (-2, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
