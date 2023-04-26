import numpy as np
import random
from board import Board

def randomizeSudoku(board):
    """
    Fill mutable cells on the board with random values between 1-9 that are not already in the 
    subgrid (3x3)

    args:
        board(Board): the board to randomize
        
    returns:
        (numpy.ndarray) the randomized board
    """
    subgrid_idx = [0, 3, 6]
    random_board = Board(board.grid.copy())

    for r in subgrid_idx:
        for c in subgrid_idx:
            random_board = np.where(random_board == 0, random.choice([i for i in range(1, 10) if i not in random_board.get_subgrid(r, c)]), random_board)
    return random_board
