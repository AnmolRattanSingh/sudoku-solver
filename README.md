# Simulated Annealing Sudoku Solver

## Contributors: Rucha Dave, Anmol Sandhu

## Overview

This project implements a simulated annealing algorithm to solve Sudoku puzzles. Sudoku is a logic puzzle that involves filling a 9x9 grid with numbers so that each row, column, and 3x3 subgrid contains all the numbers from 1 to 9. The algorithm uses a cost function to evaluate the quality of a particular Sudoku board configuration and then iteratively improves upon it using a combination of randomization and probability-based moves. The algorithm terminates when a board configuration with zero errors is found or when a pre-defined maximum number of iterations is reached.

## Usage

To use the program, simply run the `main.py` script. The script contains a sample Sudoku puzzle that the algorithm will attempt to solve. If the algorithm is successful, the solution will be printed to the console along with the time taken to find it.

## Dependencies

The program requires the following dependencies:

- `time`: used for timing the execution of the algorithm
- `numpy`: used for handling multidimensional arrays in Python
- `pytest`: used for unit testing

To install the dependencies, run the following command in the terminal:

```
pip install -r requirements.txt
```

## Implementation

The algorithm is implemented in Python and consists of two main components: the `Board` class and the `board_util` module.

### `Board` Class

The `Board` class represents a Sudoku board configuration. It contains methods for initializing a board with a given puzzle, setting and getting cell values, and checking whether a particular cell value is valid.

### `board_util` Module

The `board_util` module contains various utility functions used by the simulated annealing algorithm. These include:

- `initialTemp(board)`: calculates the initial temperature for the simulated annealing algorithm based on the initial cost of the board
- `randomizeSudoku(board)`: generates a random Sudoku board configuration with the correct subgrid structure
- `chooseNewBoard(temp_board, board, cost, temp)`: generates a new board configuration by making a probability-based move from the current board
- `totalIterations(board)`: calculates the total number of iterations to be performed by the simulated annealing algorithm based on the size of the Sudoku board. The principled approach to find the total number of iterations is to calculate the square of the number of mutable cells on the board. But we found out during our testing that using the square root gave faster results.
- `boardCost(board)`: calculates the cost of the board based on the number of errors in the rows and columns

## Conclusion

Simulated annealing is a powerful optimization algorithm that can be used to solve a wide range of optimization problems, including Sudoku puzzles. The algorithm is relatively simple to implement and can be used to find near-optimal solutions to large and complex problems.
