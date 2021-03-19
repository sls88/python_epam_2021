"""Homework 5.1."""
import datetime
import sys
from typing import Optional


class Student:
    """Create student."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: "Homework") -> Optional["Homework"]:
        """Сheck if homework is done.

        Args:
            homework: Instance of class Homework

        Returns:
            The return value. If the time for completing the task has not expired - return instance of class Homework
                            else - print the message to sys.stdout: "You are late" and return None
        """
        self.homework = homework
        if self.homework.is_active():
            return self.homework
        sys.stdout.write("You are late")


class Teacher:
    """Create teacher."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

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
