"""TEST Homework 3.1."""

from hw.hw3.hw3_task1 import cache


@cache(times=2)
def f():
    return input("? ")


def test_cache(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda msg: "1")
    assert f() == "1"
    assert f() == "1"
    assert f() == "1"
    monkeypatch.setattr("builtins.input", lambda msg: "2")
    assert f() == "2"
