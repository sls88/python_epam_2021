"""Homework 7.2."""


def clear_string_by_recursion(s: str) -> str:
    """Return string after backspace corrections. # means a backspace character.

    Args:
        s: string with "#"

    Returns:
        The return value. Correct string.
    """
    ind = s.find("#")
    if ind == -1:
        return s
    elif ind == 0:
        return clear_string_by_recursion(s[1:])
    elif s[ind - 1] == "#":
        return clear_string_by_recursion(s[:ind] + s[ind + 1 :])
    else:
        return clear_string_by_recursion(s[: ind - 1] + s[ind + 1 :])


def backspace_compare(first: str, second: str) -> bool:
    """Return if they are equal when both are typed into empty text editors. # means a backspace character.

    Args:
        first: first string with "#"
        second: first string with "#"

    Returns:
        The return value. True if first string = second, after chenges.
    """
    return clear_string_by_recursion(first) == clear_string_by_recursion(second)


def clear_string(s: str) -> str:
    """Return string after backspace corrections. # means a backspace character.

    Args:
        s: string with "#"

    Returns:
        The return value. Correct string.
    """
    st = s
    while st.find("#") != -1:
        ind = st.find("#")
        if ind == 0:
            st = st[1:]
        elif st[ind - 1] == "#":
            st = st[:ind] + st[ind + 1 :]
        else:
            st = st[: ind - 1] + st[ind + 1 :]
    return st


def backspace_compare2(first: str, second: str) -> bool:
    """Return if they are equal when both are typed into empty text editors. # means a backspace character.

    Args:
        first: first string with "#"
        second: first string with "#"

    Returns:
        The return value. True if first string = second, after chenges.
    """
    return clear_string(first) == clear_string(second)
