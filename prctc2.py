# Tic Tac Toe game in Python without Pygame library

def draw_board(board):
    print('     |     |')
    print('  ' + board[0] + '  |  ' + board[1] + '  |  ' + board[2])
    print('_____|_____|_____')
    print('     |     |')
    print('  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5])
    print('_____|_____|_____')
    print('     |     |')
    print('  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8])
    print('     |     |')

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return True
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return True

    return False

def get_move(player, board):
    valid_move = False
    while not valid_move:
        move = input('Player ' + player + ', enter a valid move (1-9): ')
        if move.isdigit():
            move = int(move) - 1
            if move >= 0 and move <= 8 and board[move] == ' ':
                valid_move = True

    return move

def play_game():
    board = [' '] * 9
    draw_board(board)

    player = 'X'
    while True:
        move = get_move(player, board)
        board[move] = player
        draw_board(board)

        if check_win(board):
            print('Player ' + player + ' wins!')
            break

        if ' ' not in board:
            print('The game is a tie!')
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

if __name__ == '__main__':
    play_game()
