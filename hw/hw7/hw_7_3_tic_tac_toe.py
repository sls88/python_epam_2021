"""Homework 7.3."""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Analyze the results of the game.

    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!".

    Args:
        board: board list

    Returns:
        The return value. Result
    """
    x = sum(board, [])
    horizontal = {
        x[0 + i] for i in range(0, 9, 3) if x[0 + i] == x[1 + i] == x[2 + i] != "-"
    }
    vertical = {x[0 + i] for i in range(3) if x[0 + i] == x[3 + i] == x[6 + i] != "-"}
    cross = (
        {x[4]}
        if (x[0] == x[4] == x[8] != "-" or x[2] == x[4] == x[6] != "-")
        else set()
    )
    rez = horizontal | vertical | cross
    if len(rez) == 2:
        return "draw!"
    elif len(rez) == 1:
        return f"{str(*rez)} wins!"
    elif "-" in x:
        return "unfinished!"
    return "draw!"
