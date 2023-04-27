import numpy as np
import random
from board import Board
from copy import deepcopy


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

def notFixedInSubgrid(board, chosen_subgrid_idx):
    """
    Find all the cells in a subgrid (3x3) that are not fixed (mutable).
    
    args:
        board(Board): the board to find "not fixed" values from

    returns:
        (list of lists of ints) list of lists containing the rows and columns of the cells that are not fixed
        
    """
    not_fixed_in_subgrid = []
    fixed_board = board.fixedValues

    for r in range(3):
        for c in range(3):
            if fixed_board[r + chosen_subgrid_idx[0], c + chosen_subgrid_idx[1]] == 0:
                not_fixed_in_subgrid.append([r + chosen_subgrid_idx[0], c + chosen_subgrid_idx[1]])
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
    not_fixed_values = notFixedInSubgrid(board, chosen_subgrid_idx)
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
    for r in range(9):
        cost += len(board.getRow(r)) - len(set(board.getRow(r)))
    # check duplicate values in columns
    for c in range(9):
        cost += len(board.getCol(c)) - len(set(board.getCol(c)))
    
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

def chooseNewBoard(sudoku_board, cost):
    """
    Choose a new board based on current board and temperature.

    args:
        board(Board): the current board
        cost(int): the current temperature

    returns:
        (Board) the new board
    """
    cell_1, cell_2 = selectTwoCells(sudoku_board)
    board_proposed = flipCells(sudoku_board, cell_1, cell_2)
    cost_proposed = boardCost(board_proposed)
    delta_cost = cost_proposed - cost
    prob = np.exp(-delta_cost / cost)
    if np.random.uniform(1,0,1) < prob:
        return board_proposed, cost_proposed
    else:
        return sudoku_board, cost
