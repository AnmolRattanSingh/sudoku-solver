from board import Board
import board_util as bu
import time
import numpy as np

puzzle = [0, 0, 3, 0, 2, 0, 6, 0, 0,
          9, 0, 0, 3, 0, 5, 0, 0, 1,
          0, 0, 1, 8, 0, 6, 4, 0, 0,
          0, 0, 8, 1, 0, 2, 9, 0, 0,
          7, 0, 0, 0, 0, 0, 0, 0, 8,
          0, 0, 6, 7, 0, 8, 2, 0, 0,
          0, 0, 2, 6, 0, 9, 5, 0, 0,
          8, 0, 0, 2, 0, 3, 0, 0, 9,
          0, 0, 5, 0, 1, 0, 3, 0, 0]

board = Board(puzzle)
print("Initial board:", board)
time.sleep(3)

# If temperature reaches 0 and solution is still not found, restart process with new random Sudoku
print("Generating random Sudoku solution from scratch")
time.sleep(3)
solution_found = False

# time how long it takes to find a solution
start_time = time.time()
while not solution_found:
    temp_decrease = 0.99 # Decay rate for temperature
    stuck_counter = 0 # Counter for number of times worse solution is accepted
    
    # Start by randomly finding a solution to the Sudoku. This always has correct subgrids (not
    # checked for row and columns)
    temp_board = bu.randomizeSudoku(board)
    temp = bu.initialTemp(board) 
    cost = bu.boardCost(temp_board) # Total errors in the board (row and column repeats)
    iterations = bu.totalIterations(board)

    # If cost < 0, this means that the solution was found.
    if cost <= 0:
        solution_found = True

    while not solution_found:
        previous_cost = cost
        # Pick a new board for each iteration and add the cost difference to the total cost of the 
        # board, breaking if cost reaches 0.
        for i in range(iterations):
            temp_board, cost_diff = bu.chooseNewBoard(temp_board, board, cost, temp)
            cost += cost_diff
            if cost <= 0:
                solution_found = True
                break

        # Decrement temperature and check for solution
        temp *= temp_decrease
        if cost <= 0:
            solution_found = True
        
        # If overall cost has increased, increment stuck
        elif cost >= previous_cost:
            stuck_counter += 1
        else:
            stuck_counter = 0

        # If high stuck counter, increase temperature
        if stuck_counter >= 100:
            temp += 2
        if bu.boardCost(temp_board) == 0:
            print("Solution Found: ", bu.boardCost(temp_board))
            print(temp_board)
            break

# Print time taken to find solution
print("Time taken: ", time.time() - start_time)
