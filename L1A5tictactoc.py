import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def available_moves():
    return [i for i in range(9) if board[i] == " "]

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = "O"

print("🎮 Tic Tac Toe - Human vs AI")
print("You are X | AI is O")
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    print_board()

    move = int(input("Your move (1-9): ")) - 1
    if move not in available_moves():
        print("Invalid move. Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("🎉 You win!")
        break

    if is_draw():
        print_board()
        print("🤝 It's a draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI wins!")
        break

    if is_draw():
        print_board()
        print("🤝 It's a draw!")
        break
