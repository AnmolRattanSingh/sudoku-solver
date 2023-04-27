from board import Board
import board_util as bu


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
print(board)

solution_found = False
while not solution_found:
    temp_decrease = 0.99
    stuck_counter = 0

    new_board = bu.randomizeSudoku(board)
    temp = bu.initialTemp(new_board)
    cost = bu.boardCost(new_board)
    iterations = bu.totalIterations(board)

    if cost <= 0:
        solution_found = True

    while not solution_found:
        previous_cost = cost
        for i in range(iterations):
            new_state, new_cost = bu.chooseNewBoard(new_board, cost)
            cost += new_cost
            if cost <= 0:
                solution_found = True
                break
        temp *= temp_decrease
        if cost <= 0:
            solution_found = True
        elif cost >= previous_cost:
            stuck_counter += 1
        if stuck_counter >= 100:
            temp += 2
        if bu.boardCost(new_board) == 0:
            print(new_board)
            break
    

    # cell1, cell2 = bu.selectTwoCells(new_board)
    # print(cell1, new_board.getVal(*cell1))
    # print(cell2, new_board.getVal(*cell2))
    # print(new_board)

    # bu.flipCells(new_board, cell1, cell2)
    # print(new_board)
    # print(bu.boardCost(new_board))
