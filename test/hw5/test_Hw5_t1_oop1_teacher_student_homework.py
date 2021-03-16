"""TEST Homework 5.1."""
import datetime

import pytest

from hw.hw5.Hw5_t1_oop1 import Student, Teacher


@pytest.fixture()
def instance_class_teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def instance_class_student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def instance_expired_homework(instance_class_teacher):
    teacher = instance_class_teacher
    return teacher.create_homework("Learn functions", 0)


@pytest.fixture()
def instance_second_homework_oop_homework(instance_class_teacher):
    teacher = instance_class_teacher
    return teacher.create_homework("create 2 simple classes", 5)


def test_teacher_first_name(instance_class_teacher):
    teacher = instance_class_teacher
    actual_result = teacher.first_name

    assert actual_result == "Daniil"


def test_student_last_name(instance_class_student):
    student = instance_class_student
    actual_result = student.last_name

    assert actual_result == "Petrov"


def test_expired_homework_created(instance_class_teacher):
    teacher = instance_class_teacher
    expired_homework = teacher.create_homework("Learn functions", 0)
    actual_result = expired_homework.created

    assert isinstance(actual_result, type(datetime.datetime.now()))


def test_expired_homework_deadline(instance_expired_homework):
    expired_homework = instance_expired_homework
    actual_result = expired_homework.deadline

    assert actual_result == datetime.timedelta(days=0)


def test_expired_homework_text(instance_expired_homework):
    expired_homework = instance_expired_homework
    actual_result = expired_homework.text

    assert actual_result == "Learn functions"


def test_second_homework_oop_homework_deadline(instance_second_homework_oop_homework):
    oop_homework = instance_second_homework_oop_homework
    actual_result = oop_homework.deadline

    assert actual_result == datetime.timedelta(days=5)


def test_student_do_homework_oop_homework(
    instance_class_student, instance_second_homework_oop_homework
):
    student = instance_class_student
    oop_homework = instance_second_homework_oop_homework
    actual_result = student.do_homework(oop_homework)

    assert actual_result == oop_homework


def test_student_do_homework_expired_homework(
    instance_class_student, instance_expired_homework, capsys
):
    student = instance_class_student
    expired_homework = instance_expired_homework
    actual_result = student.do_homework(expired_homework)
    captured = capsys.readouterr()

    assert captured.out == "You are late"
    assert actual_result is None
