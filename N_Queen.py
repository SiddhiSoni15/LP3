def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # Base case: if all queens are placed
    if row == n:
        print_board(board)
        return True  # Found one solution

    res = False
    # Try placing queen in all columns of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place queen
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = '.'  # Backtrack

    return res


def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")


# ---------- MAIN CODE ----------
if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    n_queens(n)


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
