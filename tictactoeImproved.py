'''
Tic-Tac-Toe: Improved
Author: Eric Roberto Silva
'''
def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{color_text(board[0])}|{color_text(board[1])}|{color_text(board[2])}")
    print('-+-+-')
    print(f"{color_text(board[3])}|{color_text(board[4])}|{color_text(board[5])}")
    print('-+-+-')
    print(f"{color_text(board[6])}|{color_text(board[7])}|{color_text(board[8])}")
    print()

def color_text(text):
    if text == "x":
        return f"\033[1;31m{text}\033[1;37m"
    elif text == "o":
        return f"\033[1;32m{text}\033[1;37m"
    else:
        return text
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    if player == "x":
        print("\033[1;31m ")
    else:
        print("\033[1;32m ")
    square = int(input(((f"{player}'s turn to choose a square (1-9): "))))
    board[square - 1] = player
    print("\033[1;37m ")

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()