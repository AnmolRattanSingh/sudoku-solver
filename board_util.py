import numpy as np
import random
from board import Board
from copy import deepcopy
import math


def randomizeSudoku(board):
    """
    Fill mutable cells on the board with random values between 1-9 that are not already in the
    subgrid (3x3)

    args:
        board(Board): the board to randomize

    returns:
        (Board) the randomized board
    """
    random_board = deepcopy(board)

    for r in range(9):
        for c in range(9):
            if random_board.getVal(r, c) == 0:
                rand_val = random.choice(
                    [i for i in range(1, 10) if i not in random_board.getSubgrid(r, c)]
                )
                random_board.setVal(r, c, rand_val)

    return random_board

def notFixedInSubgrid(board, row, col):
    """
    Find all the cells in a subgrid (3x3) that are not fixed (mutable).
    
    args:
        board(Board): the board to find "not fixed" values from

    returns:
        (list of lists of ints) list of lists containing the rows and columns of the cells that are not fixed
        
    """
    not_fixed_in_subgrid = []
    fixed_board = board.fixedValues

    row_start = row - row % 3
    col_start = col - col % 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if fixed_board[r][c] == 0:
                not_fixed_in_subgrid.append([r, c])

    return not_fixed_in_subgrid

def selectTwoCells(board):
    """
    Select two random cells from a random subgrid (3x3) of the board.

    args:
        board(Board): the board to select two random cells from

    returns:
        (tuple of lists of ints) tuple containing 2 lists representing the rows and columns of the two cells
        returned [(r, c), (r, c)]
    """
    chosen_subgrid_idx = [random.choice([0, 3, 6]), random.choice([0, 3, 6])]
    not_fixed_values = notFixedInSubgrid(board, *chosen_subgrid_idx)
    cell_1 = random.choice(not_fixed_values)
    not_fixed_values.remove(cell_1)
    cell_2 = random.choice(not_fixed_values)

    return cell_1, cell_2
    

def flipCells(board, cell_1, cell_2):
    """
    Interchange the values of two cells on the board in place.

    args:
        board(Board): the board to flip cells on
        cell_1(tuple): the first cell to flip (represented as two integers (r, c))
        cell_2(tuple): the second cell to flip (represented as two integers (r, c))

    returns:
        (Board) the board with the flipped cells
    """
    new_board = deepcopy(board)
    
    tmp = new_board.getVal(cell_1[0], cell_1[1])
    new_board.setVal(cell_1[0], cell_1[1], new_board.getVal(cell_2[0], cell_2[1]))
    new_board.setVal(cell_2[0], cell_2[1], tmp)

    return new_board

def rowColCost(board, r, c):
    """
    Calculate the cost of a row on the board.

    args:
        board(Board): the board whose row cost is to be calculated
        r(int): the row to calculate the cost for

    returns:
        (int) the cost of the row
    """
    return (9 - len(np.unique(board.getRow(r))) + (9 - len(np.unique(board.getCol(c)))))

def boardCost(board):
    """
    Calculate sum of duplicate values in each row and column of the board.

    args:
        board(Board): the board whose cost is to be calculated

    returns:
        (int) the cost of the board
    """
    cost = 0
    # check duplicate values in rows
    for i in range(9):
        cost += rowColCost(board, i, i)

    return cost

def initialTemp(board):
    """
    Calculate the initial temperature for the simulated annealing algorithm.
    The initial temperature is equal to the standard deviation of the cost
    of 10 random boards.
    
    args:
        board(Board): the board to calculate the initial temperature for

    returns:
        (float) the initial temperature
    """
    costs = []

    for _ in range(10):
        cell_1, cell_2 = selectTwoCells(board)
        board_proposed = flipCells(board, cell_1, cell_2)
        costs.append(boardCost(board_proposed))
    
    return np.std(costs)

def totalIterations(board):
    """
    Calculate the total number of iterations for the simulated annealing algorithm.
    The total number of iterations is equal to the square of the number of mutable 
    cells on the board.
    
    args:
        board(Board): the board to calculate the total number of iterations for

    returns:
        (int) the total number of iterations to run for each temperature
    """
    return len(np.where(board.fixedValues == 0)) ** 2

def proposedState(current_board, initial_board):
    # pass in random subgrid to getSubgridSum
    subgrid_sum = current_board.getSubgridSum(
        initial_board.getSubgrid(random.choice([0, 3, 6]), random.choice([0, 3, 6]), fixed=True)
    )
    if subgrid_sum > 6:
        return current_board, 0
    cell_1, cell_2 = selectTwoCells(current_board)
    board_proposed = flipCells(current_board, cell_1, cell_2)

    return board_proposed, (cell_1, cell_2)

def chooseNewBoard(current_board, initial_board, cost, temp):
    """
    Choose a new board based on current board and temperature.

    args:
        board(Board): the current board
        cost(int): the current board cost (total errors)
        temp(float): the current temperature

    returns:
        (Board) the new board
    """
    board_proposed, (cell_1, cell_2) = proposedState(current_board, initial_board)
    current_cost = rowColCost(current_board, cell_1[0], cell_1[1]) + rowColCost(current_board, cell_2[0], cell_2[1])
    cost_proposed = rowColCost(board_proposed, cell_1[0], cell_1[1]) + rowColCost(board_proposed, cell_2[0], cell_2[1])
    print("cost after: ", cost_proposed)
    delta_cost = cost_proposed - current_cost
    prob = math.exp(-delta_cost / temp)
    if np.random.uniform(1,0,1) < prob:
        return board_proposed, delta_cost
    else:
        return current_board, 0
