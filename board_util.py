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
            if random_board.get_val(r,c) == 0:
                rand_val = random.choice([i for i in range(1, 10) if i not in random_board.get_subgrid(r, c)])
                random_board.set_val(r,c, rand_val)
        
    return random_board
