# n-Queens Problem Using Backtracking

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    # Check same row (any column)
    for j in range(n):
        if j != col and board[row][j] == 1:
            return False

    # Check same column (any row)
    for i in range(n):
        if i != row and board[i][col] == 1:
            return False

    # Check all four diagonal directions
    # up-left
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1

    # up-right
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1; j += 1

    # down-left
    i, j = row + 1, col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1; j -= 1

    # down-right
    i, j = row + 1, col + 1
    while i < n and j < n:
        if board[i][j] == 1:
            return False
        i += 1; j += 1

    return True

def solve_nqueens(board, col, n):
    if col >= n:
        print_board(board)
        return True

    for row in range(n):
        # If a queen is already placed in this column at this row, skip placing again
        if board[row][col] == 1:
            # move to next column
            if solve_nqueens(board, col + 1, n):
                return True
            # if that didn't lead to a solution, continue trying other rows in this column
            continue

        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, col + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

# Driver Code
n = int(input("Enter the size of the board (n): "))
first_row = int(input(f"Enter row index for first queen (0 to {n-1}): "))
first_col = int(input(f"Enter column index for first queen (0 to {n-1}): "))

# Initialize board
board = [[0 for _ in range(n)] for _ in range(n)]
board[first_row][first_col] = 1  # Place first queen

# Solve remaining queens starting from column 0 (skips already placed queen)
if solve_nqueens(board, 0, n):
    print("\nFinal n-Queens Matrix:")
    print_board(board)
else:
    print("\nNo solution exists with the given first queen position.")


# The n-Queens problem is a classic example of backtracking — a constraint satisfaction problem.
# The goal is to place n queens on an n×n chessboard such that no two queens attack each other.
# Queens can attack horizontally, vertically, and diagonally.
# We place queens column by column, checking safety at each step.
# If a conflict occurs, we backtrack and try a different position.
# The algorithm demonstrates how recursive trial and error can systematically explore possible configurations efficiently.

# Algorithm
# Input board size n.
# Place first queen at user-given position (row, col).
# For each column:
# Try placing a queen in each row.
# If safe (no attacks from other queens), place it.
# Recurse to next column.
# If no valid position, backtrack (remove queen).
# If all queens are placed, print board.

# Enter size of board: 4
# Enter row for first queen (0 to 3): 1
# Enter column for first queen (0 to 3): 0
# Final n-Queens Matrix:
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0

# Step	        Time Complexity	Space Complexity
# Backtracking	O(N!)	         O(N²)
# Safety Check	O(N)	         O(1)
# Total	        O(N!)	         O(N²)
