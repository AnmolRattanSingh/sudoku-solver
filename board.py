import numpy as np


class Board:
    def __init__(self, puzzle):
        """
        Initialize the board with a np.array representing a
        9x9 sudoku puzzle.

        args:
            puzzle(list): a list of 81 integers, where 0 represents an empty cell
        """
        self.grid = np.array(puzzle).reshape((9, 9))
        board_copy = self.grid.copy()
        self.fixedValues = np.where(board_copy != 0, 1, board_copy)

    def __repr__(self):
        """
        Create a formatted string representation of the board.

        returns:
            (str) a formatted string representation of the board with
            horizontal and vertical lines
        """
        lines = ["-" * 25]
        for i in range(9):
            line = "| "
            for j in range(9):
                line += str(self.grid[i][j]) + " "
                if j % 3 == 2:
                    line += "| "
            lines.append(line)
            if i % 3 == 2:
                lines.append("-" * 25)
        return "\n".join(lines)

    def getVal(self, row, col):
        """
        Get the value at a given row and column.

        args:
            row(int): the row of the cell between 0 and 8
            col(int): the column of the cell between 0 and 8

        returns:
            (int) the value at the given row and column
        """
        try:
            return self.grid[row][col]
        except IndexError:
            raise IndexError(f"Invalid row or column: {row}, {col}")

    def setVal(self, row, col, val):
        """
        Set the value at a given row and column.

        args:
            row(int): the row of the cell between 0 and 8
            col(int): the column of the cell between 0 and 8
            val(int): the value to set the cell to, between 1 and 9
        """
        self.grid[row][col] = val

    def getRow(self, row):
        """
        Get the values in a given row.

        args:
            row(int): the row of the grid between 0 and 8

        returns:
            (numpy.ndarray) the values in the given row
        """
        try:
            return self.grid[row]
        except IndexError:
            raise IndexError(f"Invalid row: {row}")

    def getCol(self, col):
        """
        Get the values in a given column.

        args:
            col(int): the column of the grid between 0 and 8

        returns:
            (numpy.ndarray) the values in the given column
        """
        return self.grid[:, col]

    def getSubgrid(self, row, col):
        """
        Get the 3x3 subgrid containing the given row and column.

        args:
            row(int): the row of the cell between 0 and 8
            col(int): the column of the cell between 0 and 8

        returns:
            (numpy.ndarray) the 3x3 subgrid containing the given row and column
        """
        row_start = row - row % 3
        col_start = col - col % 3
        return self.grid[row_start : row_start + 3, col_start : col_start + 3]
