#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os
import time
import random

rd = 0
move = None


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
        new_board[i] = player

        if player == 'X':
            result = play_out(new_board, 'O')
            score[i] = result
        else:
            result = play_out(new_board, 'X')
            score[i] = result

        new_board[i] = i

        if player == 'X':
            move = max(score, key=score.get)
        else:
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


def main():
    players = [('O', 'O'), ('X', 'X')]
    turn = 0
    wins = {'X': 0, 'O': 0, 'TIES': 0}

    # start game
    for _ in range(500):

        i = random.randint(0, 8)

        # board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        board = ['X' if x == i else x for x in range(9)]
        turn = 1

        while True:
            turn += 1

            # calculate the current player
            player = players[turn % 2]

            if turn % 2 == 1:
                play_out(board, 'X')
                choice = move
            else:
                play_out(board, 'O')
                choice = move

            board[choice] = player[1]

            if check_for_win(board, player[1]) is True:
                # print(f'Game Over! {player[0].upper()} WINS!!!')
                wins[player[1]] += 1
                print(wins)
                break
            elif turn == 9:
                wins['TIES'] += 1
                # print('Scratch... Game Over!')
                print(wins)
                break


# run main program
if __name__ == '__main__':
    main()
