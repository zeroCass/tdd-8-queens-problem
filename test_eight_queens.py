from eight_queens import *

def test_solution_function_exists():
    """ function that  test if is_solution_to_8_queens_problem exists """
    result = is_solution_to_8_queens_problem(board = [])
    assert isinstance(result, int) is True

