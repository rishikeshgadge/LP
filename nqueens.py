def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_bt(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_bt(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

def n_queens_backtracking(n):
    board = [[0] * n for _ in range(n)]
    if solve_n_queens_bt(board, 0, n):
        for row in board:
            print(row)
    else:
        print("No solution exists.")

## Branch and bound


# def solve_n_queens_bb(row, n, board, cols, diag1, diag2):
#     if row == n:
#         return True

#     for col in range(n):
#         d1 = row - col + n - 1
#         d2 = row + col
#         if not cols[col] and not diag1[d1] and not diag2[d2]:
#             board[row][col] = 1
#             cols[col] = diag1[d1] = diag2[d2] = True

#             if solve_n_queens_bb(row + 1, n, board, cols, diag1, diag2):
#                 return True

#             board[row][col] = 0
#             cols[col] = diag1[d1] = diag2[d2] = False

#     return False

# def n_queens_branch_and_bound(n):
#     board = [[0] * n for _ in range(n)]
#     cols = [False] * n
#     diag1 = [False] * (2 * n - 1)
#     diag2 = [False] * (2 * n - 1)

#     if solve_n_queens_bb(0, n, board, cols, diag1, diag2):
#         for row in board:
#             print(row)
#     else:
#         print("No solution exists.")
