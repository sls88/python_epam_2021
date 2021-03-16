"""TEST Homework 4.3."""
from hw.hw4.Homework_4_task3 import my_precious_logger


def test_my_precious_logger_stderr(capsys):
    my_precious_logger("error: something")
    captured = capsys.readouterr()
    assert captured.err == "error: something"


def test_my_precious_logger_stdout(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"
