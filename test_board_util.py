"""
Tests for the Board Utils functions
"""
import pytest
from board_util import *

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

NOT_FIXED_IN_SUBGRID_CASES = [
    # Random subgrids to test from the TEST_BOARD
    # (row, column)
    (0, 0),
    (1, 6),
    (2, 5),
]
ROW_COL_COST_CASES = [
    # Test that the cost of a row or column is calculated correctly for the TEST_BOARD
    # (cost, row, column)
    (10, 0, 0),
    (9, 1, 0),
    (6, 3, 3),
]

def test_randomizeSudoku():
    """
    Test that the randomizeSudoku function randomizes the board correctly
    """
    random_board = randomizeSudoku(TEST_BOARD)
    assert np.not_equal(random_board.grid, TEST_BOARD.grid).any()

    # test each subgrid is contains unique values 1-9
    for r in range(3):
        for c in range(3):
            subgrid = random_board.getSubgrid(r * 3, c * 3)
            assert len(np.unique(subgrid)) == 9

@pytest.mark.parametrize("subgrid_cell", NOT_FIXED_IN_SUBGRID_CASES)
def test_notFixedInSubgrid(subgrid_cell):
    """
    Test that the notFixedInSubgrid function returns the correct values
    """
    not_fixed_coords = notFixedInSubgrid(TEST_BOARD, subgrid_cell[0], subgrid_cell[1])
    # loop through rows and columns returned by notFixedInSubgrid
    for r, c in not_fixed_coords:
        # check that the value at the row and column is not fixed
        assert TEST_BOARD.fixedValues[r, c] == 0
    print(np.count_nonzero(TEST_BOARD.getSubgrid(subgrid_cell[0], subgrid_cell[1])))
    # check that the number of returned rows and columns is correct
    assert len(not_fixed_coords) == (9 - np.count_nonzero(TEST_BOARD.getSubgrid(subgrid_cell[0], subgrid_cell[1])))

def test_selectTwoCells():
    """
    Test that the selectTwoCells function selects two cells that are not fixed
    """
    cell_1, cell_2 = selectTwoCells(TEST_BOARD)
    # check that the returned cells are not fixed
    assert TEST_BOARD.fixedValues[cell_1[0], cell_1[1]] == 0
    assert TEST_BOARD.fixedValues[cell_2[0], cell_2[1]] == 0

def test_flipCells():
    """
    Test that the flipCells function flips the values of two cells on the board
    using a temporary board
    """
    cell_1, cell_2 = selectTwoCells(TEST_BOARD)
    temp_board = deepcopy(TEST_BOARD)
    flipCells(temp_board, cell_1, cell_2)
    # check that the values of the two cells are flipped
    assert temp_board.grid[cell_1[0], cell_1[1]] == TEST_BOARD.grid[cell_2[0], cell_2[1]]
    assert temp_board.grid[cell_2[0], cell_2[1]] == TEST_BOARD.grid[cell_1[0], cell_1[1]]
    # check that the values of the other cells are the same
    for r in range(9):
        for c in range(9):
            if (r, c) != cell_1 and (r, c) != cell_2:
                assert temp_board.grid[r, c] == TEST_BOARD.grid[r, c]

@pytest.mark.parametrize("cost, row, col", ROW_COL_COST_CASES)
def test_rowColCost(cost, row, col):
    """
    Test that the rowColCost function returns the correct values
    """
    assert rowColCost(TEST_BOARD, row, col) == cost

def test_totalIterations():
    """
    Test that the totalIterations function returns the correct number of iterations
    """
    assert totalIterations(TEST_BOARD) == int(49 ** 0.5)
    