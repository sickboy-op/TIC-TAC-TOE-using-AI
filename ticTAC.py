import math

board = [' ' for _ in range(9)]

def print_board():
    """Print the current board"""
    print(f"""
     {board[0]} | {board[1]} | {board[2]}
    ---+---+---
     {board[3]} | {board[4]} | {board[5]}
    ---+---+---
     {board[6]} | {board[7]} | {board[8]}
    """)

def check_win(player):
    """Check if given player has won"""
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def check_draw():
    """Check if the board is full"""
    return ' ' not in board

def player_move():
    """Player chooses a move"""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1-9.")


def minimax(is_maximizing, alpha, beta):
    """Minimax algorithm with Alpha-Beta pruning"""
    if check_win('O'):
        return 1
    if check_win('X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False, alpha, beta)
                board[i] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True, alpha, beta)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def ai_move():
    """AI makes the best move using minimax"""
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'
    print(f"AI chose position {best_move+1}")



def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    print_board()

    while True:
        
        player_move()
        print_board()
        if check_win('X'):
            print(" You win!")
            break
        if check_draw():
            print("It's a draw!")
            break

        
        ai_move()
        print_board()
        if check_win('O'):
            print(" Computer wins!")
            break
        if check_draw():
            print("It's a draw!")
            break

    input("\nPress Enter to exit...") 

if __name__ == "__main__":
    play_game()
