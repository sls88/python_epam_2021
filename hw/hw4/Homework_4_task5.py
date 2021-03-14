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
        lst = [
            list(
                map(
                    str,
                    [
                        1 + i * 15,
                        2 + i * 15,
                        "Fizz",
                        4 + i * 15,
                        "Buzz",
                        "Fizz",
                        7 + i * 15,
                        8 + i * 15,
                        "Fizz",
                        "Buzz",
                        11 + i * 15,
                        "Fizz",
                        13 + i * 15,
                        14 + i * 15,
                        "FizzBuzz",
                    ],
                )
            )
            for i in range(n // 15 + 1)
        ]
        for j in sum(lst, [])[:n]:
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

        def fizz_buzz(seq_lst: List[str]) -> List[str]:
            """Process FizzBuzz.

            Args:
                seq_lst: sequence

            Returns:
                The return value. Change sequence with FizzBuzz elements
            """
            for i in range(14, len(seq_lst), 15):
                seq_lst[i] = "FizzBuzz"
            return seq_lst

        def fizz(seq_lst: List[str]) -> List[str]:
            """Process Fizz.

            Args:
                seq_lst: sequence

            Returns:
                The return value. Change sequence with Fizz elements
            """
            for i in range(2, len(seq_lst), 3):
                seq_lst[i] = "Fizz"
            return seq_lst

        def buzz(seq_lst: List[str]) -> List[str]:
            """Process Buzz.

            Args:
                seq_lst: sequence

            Returns:
                The return value. Change sequence with Buzz elements
            """
            for i in range(4, len(seq_lst), 5):
                seq_lst[i] = "Buzz"
            return seq_lst

        for j in fizz_buzz(fizz(buzz([str(i) for i in range(1, n + 1)]))):
            yield j

    return fizz_buzz_generator()
