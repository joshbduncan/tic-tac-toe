#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os

def welcome_screen():
    os.system('clear')
    print('\n- - - - - - - - - - - - -')
    print('- - - - - - - - - - - - -')
    print(' Welcome to Tic-Tac-Toe!')
    print('- - - - - - - - - - - - -')
    print('- - - - - - - - - - - - -')

def collect_player_names():
    p1 = input('\nEnter name of Player 1: ')
    p2 = input('Enter name of Player 2: ')
    return [(p2, 'O'),(p1, 'X')]

def print_board(board):
    print('\n- - - - - - - - - - - - -')
    print(' Welcome to Tic-Tac-Toe!')
    print('- - - - - - - - - - - - -')

    for row in board:
        print('+---+---+---+')
        print(f'| {row[0]} | {row[1]} | {row[2]} |')
    print('+---+---+---+')

def check_for_win(board):
    wins = [['X', 'X', 'X'], ['O', 'O', 'O']]

    top_to_bottom = [board[0][0], board[1][1], board[2][2]]
    bottom_to_top = [board[0][2], board[1][1], board[2][0]]

    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        row = [board[i][0], board[i][1], board[i][2]]

        if col in wins or row in wins or top_to_bottom in wins or bottom_to_top in wins:
            return False

    return True

def guess(turn, players, board):
    os.system('clear')
    print_board(board)

    player, mark = players[turn % 2][0], players[turn % 2][1]

    try:
        # ask current player for their desired postion
        choice = int(input(f'\n{player} which position would you like to mark? (1-9): '))

        # check for an input 0
        if choice == 0:
            raise Exception()

        # set the line (0, 1, 2) and position (0, 1, 2) to play
        line = (choice - 1) // 3
        position = (choice - (line * 3)) - 1

        # check to see if the position has already been played
        # if not then play the move
        if board[line][position] in ['X', 'O']:
            print(f'Sorry position {str(choice)} has already been played. Try again.')
            guess(turn, players, board)
        else:
            board[line][position] = mark

    # exit on ctrl+c
    except KeyboardInterrupt:
        raise

    # input was not a valid number
    except:
        print('\nInvalid choice...')
        guess(turn, players, board)

    return board

def main():
    board = [['1','2','3'],['4','5','6'],['7','8','9']]

    # Welcome Screen
    welcome_screen()

    # collect player names
    players = collect_player_names()
    print(f'\n{players[1][0]} (X) vs. {players[0][0]} (O)')
    input('\nPress any key to begin!')

    turn = 0

    # start game
    while True:
        turn += 1

        ans = guess(turn, players, board)

        if check_for_win(board) is False:
            player = players[turn % 2][0]
            print('\n* * * * * * * * * *')
            print(f'Game Over! {player.upper()} WINS!!!')
            print('* * * * * * * * * * *')
            break

        # last turn, scratch game
        if turn == 9:
            print('Scratch... Game Over!')
            break

# run main program
main()
