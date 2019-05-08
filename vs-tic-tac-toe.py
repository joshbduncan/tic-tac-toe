#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os
import time

rd = 0
move = None


def welcome_screen():
    os.system('clear')
    print('\n- - - - - - - - - - - - -')
    print(' Welcome to Tic-Tac-Toe!')
    print('- - - - - - - - - - - - -')


def print_board(board):
    for i in range(0, 9, 3):
        print('+---+---+---+')
        print(f'| {board[i]} | {board[i + 1]} | {board[i + 2]} |')
    print('+---+---+---+')


def empty_indexes(board):
    return [x for x in board if x not in ['X', 'O']]


def play_out(new_board, player):
    global rd
    rd += 1
    global move

    options = empty_indexes(new_board)

    if check_for_win(new_board, 'O'):
        return -10
    elif check_for_win(new_board, 'X'):
        return 10
    elif len(options) == 0:
        return 0

    score = {}

    for i in options:
        # print(f'RD {rd}: Player {player} plays spot {i}, {options}')
        new_board[i] = player

        if player == 'X':
            result = play_out(new_board, 'O')
            score[i] = result
        else:
            result = play_out(new_board, 'X')
            score[i] = result

        # print(f'result == {result}')

        new_board[i] = i

        # print(f'score = {score}')

        # if AI is going first as X
        # move = max(score, key=score.get)

        # if AI is going second as O
        move = min(score, key=score.get)

    return sum(score.values())


def check_for_win(board, player):
    if board[0] == player and board[1] == player and board[2] == player or \
            board[3] == player and board[4] == player and board[5] == player or \
            board[6] == player and board[7] == player and board[8] == player or \
            board[0] == player and board[3] == player and board[6] == player or \
            board[1] == player and board[4] == player and board[7] == player or \
            board[2] == player and board[5] == player and board[8] == player or \
            board[0] == player and board[4] == player and board[8] == player or \
            board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False


def guess(turn, player, board):
    os.system('clear')
    print_board(board)

    while True:
        try:
            # ask current player for their desired postion
            choice = int(
                input(f'\n{player[0]} which position would you like to mark? (0-8): '))

            # check for an input 0
            if choice < 0 or choice > 8:
                print(f'Invalid choice. Please choose a position between 0 and 8...')
                time.sleep(2)
                continue

            # check to see if the position has already been played
            elif board[choice] == 'X' or board[choice] == 'O':
                print(
                    f'Sorry position {str(choice)} has already been played. Try again.')
                time.sleep(2)
                continue

            else:
                return choice

        # exit on ctrl+c
        except KeyboardInterrupt:
            raise

        # input was not a valid number
        except:
            print('\nInvalid choice. Please choose a position between 0 and 8...')
            time.sleep(2)
            continue


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Welcome Screen
    welcome_screen()

    # collect player names

    # when AI goes first as X
    # players = [('Josh', 'O'), ('AI', 'X')]

    # when AI goes second as O
    players = [('AI', 'O'), ('Josh', 'X')]

    print(f'\n{players[1][0]} (X) vs. {players[0][0]} (O)')
    input('\nPress any key to begin!')

    turn = 0

    # start game
    while True:
        turn += 1

        # calculate the current player
        player = players[turn % 2]

        # prompt the current player for their next move
        # when AI goes first as X
        # if turn % 2 == 0:

        # when AI second first as O
        if turn % 2 == 0:
            play_out(board, 'O')
            print(f'Move = {move}')
            choice = move
        else:
            choice = guess(turn, player, board)

        board[choice] = player[1]

        # check to see if the current player has won or if scratch game
        if check_for_win(board, player[1]) is True:
            os.system('clear')
            print('\n* * * * * * * * * * * * * *')
            print(f'Game Over! {player[0].upper()} WINS!!!')
            print('* * * * * * * * * * * * * *')
            print_board(board)
            print('\n')
            break
        elif turn == 9:
            print('Scratch... Game Over!')
            break

        print(f'YOUR CHOICE WAS {choice}')


# run main program
if __name__ == '__main__':
    main()
