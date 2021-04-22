"""TEST Homework 11.2."""

from hw.hw11.Hw11_2_sale_strategy import Order


def morning_discount(order: Order):
    return order.price * 0.5


def elder_discount(order: Order):
    return order.price * 0.9


def very_big_discount(order: Order):
    return order.price * 1.2


def test_first_discount():
    order = Order(100, morning_discount)

    assert order.final_price() == 50


def test_another_discount():
    order = Order(100, elder_discount)

    assert order.final_price() == 10


def test_maximum_discount():
    order = Order(100, morning_discount, elder_discount)

    assert order.final_price() == 10


def test_zero_discount():
    order = Order(100)

    assert order.final_price() == 100


def test_very_big_discount():
    order = Order(100, very_big_discount)

    assert order.final_price() == 0
