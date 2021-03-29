"""Homework 7.3."""
from typing import List


def tic_tac_toe_checker(x: List[List]) -> str:
    """Analyze the results of the game.

    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!".

    Args:
        x: board list

    Returns:
        The return value. Result
    """
    horizontal = {i[0] for i in x if i[0] != "-" and len(set(i)) == 1}
    vertical = {a for a, b, c in zip(*x) if a == b == c != "-"}
    x = sum(x, [])
    cross_l = {x[4]} if x[0] == x[4] == x[8] != "-" else set()
    cross_r = {x[4]} if x[2] == x[4] == x[6] != "-" else set()
    rez = horizontal | vertical | cross_l | cross_r
    if len(rez) == 2:
        return "draw!"
    elif len(rez) == 1:
        return f"{str(*rez)} wins!"
    elif "-" in x:
        return "unfinished!"
    return "draw!"
