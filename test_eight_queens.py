from eight_queens import *

def test_solution_function_exists():
    """ function that  test if is_solution_to_8_queens_problem exists """  
    result = is_solution_to_8_queens_problem(board = [])
    assert isinstance(result, int) is True

def test_check_if_is_valid_board():
    """ this function will test if a board input has size of 8 x 8
    the result should be -1 if is not and 1 if it is """
    board = [[1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0]]
    result = is_valid_board(board)
    assert result is True

def test_check_is_has_8_queens_in_board():
    """ check if the given board has 8 queen inside """
    board = [[1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0]]
    result = has_eight_queens(board)
    assert result is True

def test_check_if_has_no_queen_in_row():
    """ this function will test if the board has no more than one queen in the same row """
    board = [[1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0]]
    for row in range(8):
        for column in range(8):
            if board[row][column] == 1:
                result = has_queen_in_row(board, row, column)
                assert result is False

def test_check_is_has_no_queen_in_column():
    """ this funciton will check if the board has no more than one queen in the same column """
    board = [[1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0]]
    for row in range(8):
        for column in range(8):
            if board[row][column] == 1:
                result = has_queen_in_column(board, row, column)
                assert result is False

def test_check_is_has_no_queen_in_main_diagonal():
    """ this function will check if has another queen in the same diagonal
    (top-rigth and bottom left) """
    # fails in diagonal top-right (2,3 - 0,5)
    board = [[1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0]]
    for row in range(8):
        for column in range(8):
            if board[row][column] == 1:
                result = has_queen_in_main_diagonal(board, row, column)
                assert result is False

    