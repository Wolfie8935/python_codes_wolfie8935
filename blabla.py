# Advanced Tic Tac Toe game in Python without Pygame library

import random

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
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]

    # Check for tie
    if ' ' not in board:
        return 'T'

    return None

def get_move(player, board, mode):
    if mode == '1':
        if player == 'X':
            valid_move = False
            while not valid_move:
                move = input('Player ' + player + ', enter a valid move (1-9): ')
                if move.isdigit():
                    move = int(move) - 1
                    if move >= 0 and move <= 8 and board[move] == ' ':
                        valid_move = True
        else:
            move = get_ai_move(board, player)

    else:
        valid_move = False
        while not valid_move:
            move = input('Player ' + player + ', enter a valid move (1-9): ')
            if move.isdigit():
                move = int(move) - 1
                if move >= 0 and move <= 8 and board[move] == ' ':
                    valid_move = True

    return move

def get_ai_move(board, ai_player):
    opp_player = 'O' if ai_player == 'X' else 'X'

    # Check if AI can win in the next move
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_player
            if check_win(board) == ai_player:
                return i
            board[i] = ' '

    # Check if opponent can win in the next move
    for i in range(9):
        if board[i] == ' ':
        board[i] = opp_player
        if check_win(board) == opp_player:
        return i
        board[i] = ' '
        # Try to take one of the corners
        corners = [0, 2, 6, 8]
        possible_moves = []
        for i in corners:
        if board[i] == ' ':
            possible_moves.append(i)
        if len(possible_moves) > 0:
        return random.choice(possible_moves)

        # Try to take the center
        if board[4] == ' ':
        return 4

        # Take one of the sides
        sides = [1, 3, 5, 7]
        possible_moves = []
        for i in sides:
        if board[i] == ' ':
            possible_moves.append(i)
        if len(possible_moves) > 0:
        return random.choice(possible_moves)

        return None

