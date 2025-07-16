import math

# Initial empty board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print("\n")
    for i in range(3):
        row = "|".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("-------")
    print("\n")

# Check for winner
def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_conditions:
        if all(brd[i] == player for i in combo):
            return True
    return False

# Check for draw
def is_draw(brd):
    return " " not in brd

# Minimax algorithm
def minimax(brd, is_maximizing):
    if check_winner(brd, "O"):
        return 1
    if check_winner(brd, "X"):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Player move
def player_move():
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Position already taken.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number from 1 to 9.")

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O. Board positions are numbered 1 to 9.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        best_move()
        print_board()
        if check_winner(board, "O"):
            print("💻 AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
