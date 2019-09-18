#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os
import time
import copy


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


def collect_player_names():
    while True:
        p1 = input('\nEnter name of Player 1: ')
        if p1 == '':
            print('Invalid player name. Please try again.')
            continue
        else:
            break
    while True:
        p2 = input('Enter name of Player 2: ')
        if p2 == '':
            print('Invalid player name. Please try again.')
            continue
        else:
            break
    return [(p2, 'O'), (p1, 'X')]


def get_branches(board, player):
    # get all possible plays for the current board and player
    branches = []
    for pos in range(9):
        if board[pos] not in ['X', 'O']:
            branches.append((pos, copy.deepcopy(board)))
            branches[-1][1][pos] = player
    return branches


def solve(board, player, score):
    # play out the current board and calculate draw, wins, and losses
    if check_for_win(board, 'X'):
        score -= 10
        return score
    if check_for_win(board, 'O'):
        score += 10
        return score

    # get all possible branches for current board
    branches = get_branches(board, player)

    # play out the entire board from passed board
    for _, branch in branches:
        if player == 'X':
            return solve(branch, 'O', score)
        else:
            return solve(branch, 'X', score)

    # return the score for the played position
    return score


def ai_play(board, player):
    scores = {}
    branches = get_branches(board, player)

    # calculate win/loss score for each possible position
    for branch in branches:
        answer = solve(branch[1], 'O', 0)
        # add position score to scores
        scores[branch[0]] = answer

    # keep up with draw spots, win spots, and lose spots
    spots_to_play = set()
    winners = set()
    losers = set()

    # iterate through available positions
    for k, v in scores.items():
        # if the position matches the max update board
        if v == max(scores.values()):
            board[k] = 'O'

            # check to see if this is now a winning board
            if check_for_win(board, 'O'):
                winners.add(k)

            # check to see if this position creates a win for opponent
            lose_branches = get_branches(board, 'X')
            for x_branch in lose_branches:
                # if position does create loss, add it to losers
                if check_for_win(x_branch[1], 'X'):
                    losers.add(x_branch[0])
                    break
                # ...if now, add it draw spots
                else:
                    spots_to_play.add(k)
                    board[k] = k

        # reset board
        board[k] = k

    # print statistics for AI suggestion
    print('spots', spots_to_play)
    print('winners', winners)
    print('losers', losers)

    # suggest optimila play
    if len(winners) > 0:
        print(f'PLAY POSITION {list(winners)[0]}')
    elif len(losers) > 0:
        print(f'BLOCK POSITION {list(losers)[0]}')
    else:
        print(f'BEST PLAY IS {min(spots_to_play)}')

    return board


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
        if player[1] == 'O':
            ai_play(copy.deepcopy(board), 'O')
        try:
            # ask current player for their desired postion
            choice = int(
                input(f'\n{player[0]} ({player[1]}) which position would you like to mark? (0-8): '))

            # check for a valid input position
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

    # welcome screen
    welcome_screen()

    # collect player names
    players = collect_player_names()
    print(f'\n{players[1][0]} (X) vs. {players[0][0]} (O)')
    input('\nPress any key to begin!')

    turn = 0

    # start game
    while True:
        turn += 1

        # calculate the current player
        player = players[turn % 2]

        # prompt the current player for their next move
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
