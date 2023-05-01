"""
Tests for the Board class
"""
import pytest
from board import Board

PUZZLE = [0, 0, 3, 0, 2, 0, 6, 0, 0,
          9, 0, 0, 3, 0, 5, 0, 0, 1,
          0, 0, 1, 8, 0, 6, 4, 0, 0,
          0, 0, 8, 1, 0, 2, 9, 0, 0,
          7, 0, 0, 0, 0, 0, 0, 0, 8,
          0, 0, 6, 7, 0, 8, 2, 0, 0,
          0, 0, 2, 6, 0, 9, 5, 0, 0,
          8, 0, 0, 2, 0, 3, 0, 0, 9,
          0, 0, 5, 0, 1, 0, 3, 0, 0]

TEST_BOARD = Board(PUZZLE)

GET_VAL_CASES = [
    # Test value at valid row and column
    (3, (0, 2)),
    # Test value at invalid row
    (9, (1, 0)),
]

GET_VAL_EXCEPTION_CASES = [
    # Test value at invalid column
    (IndexError, (0, 10)),
    (IndexError, (3, 11)),
]

SET_VAL_CASES = [
    # Test that value at valid row and column is set appropriately
    (1, (0, 2)),
    (2, (1, 0)),
]

SET_VAL_EXCEPTION_CASES = [
    # Test that value at invalid row raises an exception
    (IndexError, (0, 12)),
    (IndexError, (3, 13)),
]

FIXED_VAL_CASES = [
    # Test that 0 in initial puzzle is converted to 0 in fixed value
    (0, (3, 1)),
    (0, (5, 4)),
    # Test that number in initial puzzle is converted to 1 in fixed value
    (1, (0, 2)),
    (1, (8, 4)),
]

GET_ROW_CASES = [
    # Test that a valid row can be accessed and all values are correct
    ([0, 0, 8, 1, 0, 2, 9, 0, 0], 3),
    ([0, 0, 2, 6, 0, 9, 5, 0, 0], 6),
]

GET_COL_CASES = [
    # Test that a valid column can be accessed and all values are correct
    ([0, 9, 0, 0, 7, 0, 0, 8, 0], 0),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0], 1),
]
    
GET_SUBGRID_CASES = [
    # Test that a valid subgrid can be accessed and all values are correct
    ([[0, 0, 3, 9, 0, 0, 0, 0, 1], 13], (0, 0)),
    ([[0, 2, 0, 3, 0, 5, 8, 0, 6], 24], (0, 3)),

    # Test that a valid subgrid can be accessed for a point not at the top left corner of the grid
    ([[0, 0, 3, 9, 0, 0, 0, 0, 1], 13], (1, 1)),
    ([[0, 2, 0, 3, 0, 5, 8, 0, 6], 24], (2, 4)),
]

def test_init_shape():
    """
    Test that board initializes to the correct shape
    """
    assert Board(PUZZLE).grid.shape == (9, 9)

@pytest.mark.parametrize("fixed_val, grid_cell", FIXED_VAL_CASES)
def test_init_fixed_val(fixed_val, grid_cell):
    """
    Test that board initializes with proper fixed values
    """
    board = Board(PUZZLE)
    assert board.fixedValues[grid_cell[0], grid_cell[1]] == fixed_val

@pytest.mark.parametrize("board_val, grid_cell", GET_VAL_CASES)
def test_getVal(board_val, grid_cell):
    """
    Test the getVal function which returns the value at a given row and column
    """
    assert board_val == TEST_BOARD.getVal(grid_cell[0], grid_cell[1])

@pytest.mark.parametrize("exception, grid_cell", GET_VAL_EXCEPTION_CASES)
def test_getVal_exception(exception, grid_cell):
    """
    Test that the getVal function raises an exception when an invalid row or column is passed
    """
    with pytest.raises(exception):
        TEST_BOARD.getVal(grid_cell[0], grid_cell[1])

@pytest.mark.parametrize("board_val, grid_cell", SET_VAL_CASES)
def test_setVal(board_val, grid_cell):
    """
    Test the setVal function which sets the value at a given row and column
    """
    temp_board = Board(PUZZLE)
    temp_board.setVal(grid_cell[0], grid_cell[1], board_val)
    assert board_val == temp_board.getVal(grid_cell[0], grid_cell[1])

@pytest.mark.parametrize("exception, grid_cell", SET_VAL_EXCEPTION_CASES)
def test_setVal_exception(exception, grid_cell):
    """
    Test that the setVal function raises an exception when an invalid row or column is passed
    """
    with pytest.raises(exception):
        TEST_BOARD.setVal(grid_cell[0], grid_cell[1], 1)

@pytest.mark.parametrize("row_val, row_num", GET_ROW_CASES)
def test_getRow(row_val, row_num):
    """
    Test the getRow function by checking that a row is returned with all the right values.
    """
    board = Board(PUZZLE)
    this_row = list(board.getRow(row_num))
    assert this_row == row_val

@pytest.mark.parametrize("row_val, row_num", GET_ROW_CASES)
def test_getRow_shape(row_val, row_num):
    """
    Test the getRow function by checking that a row is returned with the right shape.
    """
    board = Board(PUZZLE)
    this_row = board.getRow(row_num)
    assert this_row.shape == (9, )

@pytest.mark.parametrize("col_val, col_num", GET_COL_CASES)
def test_getCol(col_val, col_num):
    """
    Test the getCol function by checking that a column is returned with all the right values.
    """
    board = Board(PUZZLE)
    this_col = list(board.getCol(col_num))
    assert this_col == col_val

@pytest.mark.parametrize("col_val, col_num", GET_COL_CASES)
def test_getCol_shape(col_val, col_num):
    """
    Test the getCol function by checking that a column is returned with the right shape.
    """
    board = Board(PUZZLE)
    this_col = board.getCol(col_num)
    assert this_col.shape == (9, )

@pytest.mark.parametrize("subgrid_val, position", GET_SUBGRID_CASES)
def test_getSubgrid(subgrid_val, position):
    """
    Test the getSubgrid function by checking that a subgrid is returned with all the right values.
    """
    board = Board(PUZZLE)
    this_subgrid = board.getSubgrid(position[0], position[1]).reshape(1, 9).tolist()[0]
    assert this_subgrid == subgrid_val[0]

@pytest.mark.parametrize("subgrid_val, position", GET_SUBGRID_CASES)
def test_getSubgrid_shape(subgrid_val, position):
    """
    Test the getSubgrid function by checking that a subgrid is returned with the correct shape.
    """
    board = Board(PUZZLE)
    this_subgrid = board.getSubgrid(position[0], position[1])
    assert this_subgrid.shape == (3, 3)

@pytest.mark.parametrize("subgrid_val, position", GET_SUBGRID_CASES)
def test_getSubgridSum(subgrid_val, position):
    """
    Test that getSubgridSum works by ensuring that the sum of the subgrid is correct.
    """
    board = Board(PUZZLE)
    this_subgrid = board.getSubgrid(position[0], position[1])
    assert board.getSubgridSum(this_subgrid) == subgrid_val[1]
