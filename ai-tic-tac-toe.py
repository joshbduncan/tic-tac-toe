#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

rd = 0
move = None


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
        print(f'RD {rd}: Player {player} plays spot {i}, {options}')
        new_board[i] = player

        if player == 'X':
            result = play_out(new_board, 'O')
            score[i] = result
        else:
            result = play_out(new_board, 'X')
            score[i] = result

        print(f'result == {result}')

        new_board[i] = i

        print(f'score = {score}')

        move = max(score, key=score.get)

    return sum(score.values())


def check_for_win(board, player):
    if board[0] == player and board[1] == player and board[2] == player or \
            board[3] == player and board[4] == player and board[5] == player or \
            board[6] == player and board[7] == player and board[8] == player or \
            board[0] == player and board[3] == player and board[6] == player or \
            board[1] == player and board[4] == player and board[7] == player or \
            board[2] == player and board[5] == player and board[8] == player or \
            board[0] == player and board[4] == player and board[8] == player or \
            board[2] == player and board[1] == player and board[6] == player:
        return True
    else:
        return False


def main():
    board = ['O', 1, 'X', 'X', 4, 'X', 6, 'O', 'O']
    # print_board(board)
    play_out(board, 'X')
    print(f'Move = {move}')


if __name__ == '__main__':
    main()
