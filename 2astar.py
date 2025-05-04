# Simple Tic-Tac-Toe with basic AI (like A*)

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

def check_winner(board, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

def ai_move(board):
    # 1. Win if possible
    for i in get_empty_cells(board):
        temp = board[:]
        temp[i] = 'X'
        if check_winner(temp, 'X'):
            return i
    # 2. Block opponent's win
    for i in get_empty_cells(board):
        temp = board[:]
        temp[i] = 'O'
        if check_winner(temp, 'O'):
            return i
    # 3. Take center
    if board[4] == ' ':
        return 4
    # 4. Take corners
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i
    # 5. Take any side
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            return i
    return None

# Game loop
def play_game():
    board = [' '] * 9
    print("You are O. Enter positions (0-8):")
    print_board(board)

    while True:
        # Human move
        pos = int(input("Your move (0-8): "))
        if board[pos] != ' ':
            print("Invalid move. Try again.")
            continue
        board[pos] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("You win!")
            break
        if ' ' not in board:
            print("Draw!")
            break

        # AI move
        ai = ai_move(board)
        board[ai] = 'X'
        print("AI plays:")
        print_board(board)

        if check_winner(board, 'X'):
            print("AI wins!")
            break
        if ' ' not in board:
            print("Draw!")
            break

play_game()