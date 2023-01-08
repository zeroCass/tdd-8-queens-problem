from eight_queens import *

def test_solution_function_exists():
    """ function that  test if is_solution_to_8_queens_problem exists """  
    result = is_solution_to_8_queens_problem(board = [])
    assert isinstance(result, int) is True

def test_check_if_is_valid_board():
    """ this function will test if a board input has size of 8 x 8
    the result should be -1 if is not and 1 if it is """

    result = is_valid_board(board=[])
    assert result == True
