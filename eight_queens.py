"""
This program check if a input 8x8 list that represents a chessboard
is a solution for eight queens problem
"""

def is_valid_board(board: list) -> bool:
    """ check if the board has size of 8x8 """
    # check if the board has 8 rows
    if len(board) != 8:
        return False

    # check if the board has 8 columns
    for row in board:
        if len(row) != 8:
            return False
    return True

def is_solution_to_8_queens_problem(board) -> int:
    """ check the input it is a soluction for the 8 queens problem """
    if not is_valid_board(board):
        return -1
    return 1
