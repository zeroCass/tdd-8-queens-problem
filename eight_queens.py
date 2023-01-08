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

def has_eight_queens(board: list) -> bool:
    """ check if the board has 8 queens """
    total_queens = 0

    for row in board:
        for element in row:
            if element == 1:
                total_queens += 1
    if total_queens == 8:
        return True
    return False

def has_queen_in_row(board: list, current_row: int, curent_column: int) -> bool:
    """ check if theres another queen in the current row of the actual queen """
    for colum in range(8):
        if board[current_row][colum] == 1 and colum != curent_column:
            return True
    return False


def is_solution_to_8_queens_problem(board) -> int:
    """ check the input it is a soluction for the 8 queens problem """
    if not is_valid_board(board):
        return -1
    if not has_eight_queens(board):
        return -1
    for row in range(8):
        for column in range(8):
            if board[row][column] == 1:
                if has_queen_in_row(board, row, column):
                    return 0
    return 1
