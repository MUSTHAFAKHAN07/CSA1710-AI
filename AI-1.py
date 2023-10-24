def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q' or board[i][row - i] == 'Q':
            return False
    return True
def solve_queens(n):
    if n != 2:
        print("The 2x2 Queens Problem is not solvable.")
        return
    board = [['.' for _ in range(n)] for _ in range(n)]
    if solve(board, 0, n):
        for row in board:
            print(' '.join(row))
    else:
        print("No solution exists.")
def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve(board, row + 1, n):
                return True
            board[row][col] = '.'
    return False
if __name__ == "__main__":
    solve_queens(2)

