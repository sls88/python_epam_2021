"""Homework 6.2."""
import datetime
from typing import Optional


class DeadlineError(Exception):
    """Raise an error if the deadline occure."""

    pass


class HomeworkDoesNotExistError(Exception):
    """Raise an error if the homework to be deleted does not exist."""

    pass


class UniversityLifeForm:
    """Set first name, last name of a person."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Student(UniversityLifeForm):
    """Create student."""

    def __init__(self, *args: str) -> None:
        super().__init__(*args)

    def do_homework(
        self, homework: "Homework", solution: str
    ) -> Optional["HomeworkResult"]:
        """Сheck if homework is done.

        Args:
            homework: Instance of class Homework
            solution: solution of task

        Returns:
            The return value. If the time for completing the task has not expired -
                              return instance of class HomeworkResult
                              else - raise DeadlineError: "You are late"
        """
        self.homework = homework
        self.solution = solution
        self.end_time = datetime.datetime.now()
        if self.homework.is_active():
            return HomeworkResult(self, self.homework, self.solution, self.end_time)
        raise DeadlineError("You are late")


class Teacher(UniversityLifeForm):
    """Create teacher."""

    homework_done = {}

    def __init__(self, *args: str) -> None:
        super().__init__(*args)

    @staticmethod
    def create_homework(text: str, days_amount: int) -> "Homework":
        """Create instance of class Homework.

        Args:
            text: task text
            days_amount: amount of days to complete the task

        Returns:
            The return value. Instance of class Homework
        """
        return Homework(text, days_amount)

    @classmethod
    def check_homework(cls: "Teacher", homework_result: "HomeworkResult") -> bool:
        """Check homework for more than 5 letters.

            If the condition is met, enter satisfactory results into the dictionary "homework_done", with the key:
            "instance of class Homework", the value: "instance of class HomeworkResult"

        Args:
            homework_result: instance

        Returns:
            The return value. True if the results of the homework check are satisfactory
                              (the length of the solution is more than 5 letters)
        """
        if len(homework_result.solution) > 5:
            if homework_result.homework in cls.homework_done:
                cls.homework_done[homework_result.homework] = cls.homework_done[
                    homework_result.homework
                ] | {homework_result}
                return True
            else:
                cls.homework_done[homework_result.homework] = {homework_result}
                return True
        return False

    @classmethod
    def reset_results(cls: "Teacher", homework: "Homework" = None) -> None:
        """Reset results.

            If you transfer an instance of Homework - delete only the results of this task from homework_done, if you
            don't transfer anything, then completely reset homework_done
            if an instance of homework is passed that is not in the homework_done dictionary -
                raise HomeworkDoesNotExistError("There is no such homework")

        Args:
            homework: instance
        """
        if homework is None:
            cls.homework_done.clear()
        else:
            if homework in cls.homework_done:
                del cls.homework_done[homework]
            else:
                raise HomeworkDoesNotExistError("There is no such homework")


class Homework:
    """Create homework."""

    def __init__(self, text: str, days_amount: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=days_amount)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Сheck if the time has expired for the task.

        Returns:
            The return value. True - if the time for the task has not expired
        """
        return datetime.datetime.now() - self.created < self.deadline


class HomeworkResult:
    """Create homework result.

    Args:
        author: instance
        homework: instance
        solution: Homework text
        end_time: Time when the student completed their homework
    """

    def __init__(
        self, author: Student, homework: Homework, solution: str, end_time: datetime
    ):
        self.author = HomeworkResult.__check_type_author(author)
        self.homework = HomeworkResult.__check_type_homework(homework)
        self.solution = solution
        self.end_time = end_time

    @staticmethod
    def __check_type_homework(x: Homework) -> Homework:
        """Check the data for belonging to the class Homework.

            in case of non-compliance raise TypeError("You gave a not Homework object")

        Args:
            x: unknown data

        Returns:
            The return value. Instance to the class Homework
        """
        if isinstance(x, Homework):
            return x
        raise TypeError("You gave a not Homework object")

    @staticmethod
    def __check_type_author(x: Student) -> Student:
        """Check the data for belonging to the class Student.

            in case of non-compliance raise TypeError("You gave a not Student object")

        Args:
            x: unknown data

        Returns:
            The return value. Instance to the class Student
        """
        if isinstance(x, Student):
            return x
        raise TypeError("You gave a not Student object")
