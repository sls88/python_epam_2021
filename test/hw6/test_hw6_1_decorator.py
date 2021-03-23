"""TEST Homework 6.1."""

from hw.hw6.hw6_1_decorator import instances_counter


@instances_counter
class User:
    pass


def test_get_created_instances():
    User.count = 0
    actual_result1 = User.get_created_instances()
    user, _, _ = User(), User(), User()
    actual_result2 = user.get_created_instances()

    assert actual_result1 == 0
    assert actual_result2 == 3


def test_reset_instances_counter():
    User.count = 0
    user, _, _ = User(), User(), User()
    actual_result1 = user.reset_instances_counter()
    user = User()
    actual_result2 = user.get_created_instances()

    assert actual_result1 == 3
    assert actual_result2 == 1
