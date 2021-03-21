"""TEST Homework 6.1."""

from hw.hw6.hw6_1_decorator import instances_counter


@instances_counter
class User:
    pass


def test_methods():
    actual_result1 = User.get_created_instances()
    user, _, _ = User(), User(), User()
    actual_result2 = user.get_created_instances()
    actual_result3 = user.reset_instances_counter()

    assert actual_result1 == 0
    assert actual_result2 == 3
    assert actual_result3 == 3
