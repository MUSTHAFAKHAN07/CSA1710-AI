import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def evaluate(board):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move = None
        while player_move not in range(9):
            player_move = int(input("Enter your move (0-8): "))
            row, col = divmod(player_move, 3)
            if board[row][col] != " ":
                player_move = None
                print("Invalid move. Try again.")
        board[row][col] = "O"
        print_board(board)

        if check_win(board, "O"):
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        computer_move = find_best_move(board)
        board[computer_move[0]][computer_move[1]] = "X"
        print_board(board)

        if check_win(board, "X"):
            print("Computer wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
