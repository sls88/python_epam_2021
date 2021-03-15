"""Homework 4.5."""

from typing import Generator, List


def fizzbuzz_var1(n: int) -> Generator[str, None, None]:
    """Take a number N as an input and returns a generator that yields N FizzBuzz numbers.

        Only integers >= 1 are accepted as input

    Args:
        n: number N

    Returns:
        The return value. Generator object
    """

    def fizz_buzz_generator() -> str:
        """Generate FizzBuzz numbers.

        Returns:
            The return value. Element of FizzBuzz sequence
        """
        k = [str(i) for i in range(1, n + 15)]
        for i in range(0, n, 15):
            (
                k[i + 2],
                k[i + 5],
                k[i + 8],
                k[i + 11],
            ) = ["Fizz"] * 4
            k[i + 4], k[i + 9] = ["Buzz"] * 2
            k[i + 14] = "FizzBuzz"
        for j in k[:n]:
            yield j

    return fizz_buzz_generator()


def fizzbuzz_var2(n: int) -> Generator[str, None, None]:
    """Take a number N as an input and returns a generator that yields N FizzBuzz numbers.

        Only integers >= 1 are accepted as input

    Args:
        n: number N

    Returns:
        The return value. Generator object
    """

    def fizz_buzz_generator() -> str:
        """Generate FizzBuzz numbers.

        Returns:
            The return value. Element of FizzBuzz sequence
        """

        def fizz_buzz(lst: List[str]) -> List[str]:
            """Process FizzBuzz.

            Args:
                seq_lst: sequence

            Returns:
                The return value. Change sequence with FizzBuzz elements
            """
            seq_lst = lst
            for i in range(14, len(seq_lst), 15):
                seq_lst[i] = "FizzBuzz"
            return seq_lst

        def fizz(lst: List[str]) -> List[str]:
            """Process Fizz.

            Args:
                seq_lst: sequence

            Returns:
                The return value. Change sequence with Fizz elements
            """
            seq_lst = lst
            for i in range(2, len(seq_lst), 3):
                seq_lst[i] = "Fizz"
            return seq_lst

        def buzz(lst: List[str]) -> List[str]:
            """Process Buzz.

            Args:
                seq_lst: sequence

            Returns:
                The return value. Change sequence with Buzz elements
            """
            seq_lst = lst
            for i in range(4, len(seq_lst), 5):
                seq_lst[i] = "Buzz"
            return seq_lst

        for j in fizz_buzz(fizz(buzz([str(i) for i in range(1, n + 1)]))):
            yield j

    return fizz_buzz_generator()
