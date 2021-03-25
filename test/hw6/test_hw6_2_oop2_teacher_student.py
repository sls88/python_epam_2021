"""TEST Homework 6.2."""
import datetime

import pytest

from hw.hw6.hw6_2_oop2 import DeadlineError, HomeworkDoesNotExistError, HomeworkResult
from hw.hw6.hw6_2_oop2 import Student, Teacher


@pytest.fixture()
def instance_teacher_1():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def instance_teacher_2():
    return Teacher("Aleksandr", "Smetanin")


@pytest.fixture()
def instance_lazy_student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def instance_good_student():
    return Student("Lev", "Sokolov")


@pytest.fixture()
def instance_expired_homework(instance_teacher_1):
    oop_teacher = instance_teacher_1
    return oop_teacher.create_homework("Learn functions", 0)


@pytest.fixture()
def instance_homework_1(instance_teacher_1):
    oop_teacher = instance_teacher_1
    return oop_teacher.create_homework("Learn OOP", 1)


@pytest.fixture()
def instance_homework_2(instance_teacher_1):
    oop_teacher = instance_teacher_1
    return oop_teacher.create_homework("Read docs", 5)


@pytest.fixture()
def result_1(instance_homework_1, instance_good_student):
    good_student = instance_good_student
    homework1 = instance_homework_1
    return good_student.do_homework(homework1, "Good, big solution")


@pytest.fixture()
def result_2(instance_homework_2, instance_good_student):
    good_student = instance_good_student
    homework2 = instance_homework_2
    return good_student.do_homework(homework2, "Good, big solution second student")


@pytest.fixture()
def result_2_2(instance_homework_2, instance_good_student):
    good_student = instance_good_student
    homework2 = instance_homework_2
    return good_student.do_homework(homework2, "Good, big solution third student")


@pytest.fixture()
def result_3_bad_hw(instance_homework_2, instance_good_student):
    lazy_student = instance_good_student
    homework2 = instance_homework_2
    return lazy_student.do_homework(homework2, "done")


def test_teacher_first_name(instance_teacher_1):
    teacher1 = instance_teacher_1
    actual_result = teacher1.first_name

    assert actual_result == "Daniil"


def test_student_last_name(instance_good_student):
    good_student = instance_good_student
    actual_result = good_student.last_name

    assert actual_result == "Sokolov"


def test_expired_homework_negative(instance_lazy_student, instance_expired_homework):
    lazy_student = instance_lazy_student
    expired_homework = instance_expired_homework
    solution = "Something"
    with pytest.raises(DeadlineError, match="You are"):
        lazy_student.do_homework(expired_homework, solution)


def test_incorrect_datatype_in_class_homework_result(instance_good_student):
    student = instance_good_student
    end_time = datetime.datetime.now()
    incorrect_datatype = "fff"
    with pytest.raises(TypeError, match="You gave a not"):
        HomeworkResult(student, incorrect_datatype, "Solution", end_time)


def test_temp_identity_and_exclude_double_addition(
    instance_teacher_1, instance_teacher_2, result_1, instance_homework_1
):
    Teacher.homework_done.clear()
    homework1 = instance_homework_1
    teacher1 = instance_teacher_1
    teacher2 = instance_teacher_2
    teacher1.check_homework(result_1)
    temp_1 = teacher1.homework_done
    teacher2.check_homework(result_1)
    temp_2 = Teacher.homework_done

    assert temp_1 == temp_2
    assert len(Teacher.homework_done[homework1]) == 1


def test_bad_homework_not_added(instance_teacher_1, result_3_bad_hw):
    Teacher.homework_done.clear()
    teacher = instance_teacher_1
    teacher.check_homework(result_3_bad_hw)

    assert not Teacher.homework_done


def test_add_two_hw_results_in_one_key(
    instance_teacher_1, instance_homework_2, result_2, result_2_2
):
    Teacher.homework_done.clear()
    homework2 = instance_homework_2
    teacher = instance_teacher_1
    teacher.check_homework(result_2)
    teacher.check_homework(result_2_2)

    assert len(Teacher.homework_done[homework2]) == 2


def test_reset_results(
    instance_teacher_1,
    instance_homework_1,
    instance_homework_2,
    result_1,
    result_2,
    result_2_2,
):
    Teacher.homework_done.clear()
    homework1 = instance_homework_1
    homework2 = instance_homework_2
    teacher = instance_teacher_1
    teacher.check_homework(result_1)
    teacher.check_homework(result_2)
    teacher.check_homework(result_2_2)
    Teacher.reset_results(homework2)
    actual_result1 = len(Teacher.homework_done)
    actual_result2 = Teacher.homework_done[homework1]
    Teacher.reset_results()
    actual_result3 = Teacher.homework_done

    assert actual_result1 == 1
    assert actual_result2 == {result_1}
    assert not actual_result3


def test_reset_does_not_exist_homework(
    instance_homework_1, instance_homework_2, result_1
):
    homework1 = instance_homework_1
    homework2 = instance_homework_2
    Teacher.homework_done[homework1] = result_1
    with pytest.raises(HomeworkDoesNotExistError, match="There is no"):
        Teacher.reset_results(homework2)


def test_expired_homework_deadline(instance_expired_homework):
    expired_homework = instance_expired_homework
    actual_result = expired_homework.deadline

    assert actual_result == datetime.timedelta(days=0)


def test_expired_homework_text(instance_expired_homework):
    expired_homework = instance_expired_homework
    actual_result = expired_homework.text

    assert actual_result == "Learn functions"


def test_not_expired_homework_deadline(instance_homework_2):
    not_expired_homework = instance_homework_2
    actual_result = not_expired_homework.deadline

    assert actual_result == datetime.timedelta(days=5)
