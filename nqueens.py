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


n_queens_backtracking()