from board import Board
import board_util as bu


# puzzle = [0, 0, 3, 0, 2, 0, 6, 0, 0,
#           9, 0, 0, 3, 0, 5, 0, 0, 1,
#           0, 0, 1, 8, 0, 6, 4, 0, 0,
#           0, 0, 8, 1, 0, 2, 9, 0, 0,
#           7, 0, 0, 0, 0, 0, 0, 0, 8,
#           0, 0, 6, 7, 0, 8, 2, 0, 0,
#           0, 0, 2, 6, 0, 9, 5, 0, 0,
#           8, 0, 0, 2, 0, 3, 0, 0, 9,
#           0, 0, 5, 0, 1, 0, 3, 0, 0]


# puzzle = [0, 8, 0, 0, 0, 6, 2, 0, 0,
#           5, 0, 0, 8, 7, 0, 3, 0, 0,
#           0, 0, 0, 0, 0, 4, 0, 7, 0,
#           0, 4, 0, 2, 1, 0, 0, 3, 0,
#           0, 0, 9, 0, 0, 0, 5, 0, 0,
#           0, 0, 0, 0, 0, 7, 0, 0, 0,
#           0, 0, 0, 6, 0, 0, 0, 0, 0,
#           0, 2, 0, 3, 8, 0, 0, 1, 0,
#           4, 0, 0, 0, 0, 0, 0, 0, 2]

board = Board(puzzle)

solution_found = False
while not solution_found:
    temp_decrease = 0.99
    stuck_counter = 0

    temp_board = bu.randomizeSudoku(board)
    temp = bu.initialTemp(board)
    cost = bu.boardCost(temp_board)
    iterations = bu.totalIterations(board)


    if cost <= 0:
        solution_found = True

    while not solution_found:
        previous_cost = cost
        for i in range(iterations):
            temp_board, cost_diff = bu.chooseNewBoard(temp_board, board, cost, temp)
            cost += cost_diff
            if cost <= 0:
                solution_found = True
                # print("Solution Found: ", bu.boardCost(temp_board))
                break
        temp *= temp_decrease
        if cost <= 0:
            solution_found = True
        elif cost >= previous_cost:
            stuck_counter += 1
            print("stuck_counter", stuck_counter)
        else:
            stuck_counter = 0
        if stuck_counter >= 100:
            temp += 2
        if bu.boardCost(temp_board) == 0:
            print("Solution Found: ", bu.boardCost(temp_board))
            print(temp_board)
            break

