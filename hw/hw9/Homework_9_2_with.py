"""Homework 9.2."""
from contextlib import contextmanager
from types import TracebackType
from typing import Optional


class Supressor:
    """Catch passed exception.

    Args:
        error: error

    Returns:
        The return value. None if exception = passed exception
    """

    def __init__(self, error: Exception) -> None:
        self.error = error

    def __enter__(self) -> None:
        """Enter method."""
        pass

    def __exit__(
        self, exc_type: Exception, exc_val: Exception, exc_tb: TracebackType
    ) -> Optional[bool]:
        """Catch passed exception.

        Args:
            exc_type: The type of the caught exception, or None.
            exc_val: The caught exception object, or None.
            exc_tb: The stack trace for the caught exception, or None.

        Returns:
            The return value. True if exc_type = passed exception
        """
        if exc_type == self.error:
            return True


@contextmanager
def supressor(error: Exception) -> None:
    """Catch passed exception.

    Args:
        error: error

    Returns:
        The return value. None if exception = passed exception
    """
    try:
        yield
    except error:
        pass
