import copy


def print_board(board):
    for i in range(0, 9, 3):
        print('+---+---+---+')
        print(f'| {board[i]} | {board[i + 1]} | {board[i + 2]} |')
    print('+---+---+---+')


def get_branches(board, player):
    branches = []
    for pos in range(9):
        if board[pos] not in ['X', 'O']:
            branches.append((pos, copy.deepcopy(board)))
            branches[-1][1][pos] = player
    return branches


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


def solve(board, player, score):

    # print_board(board)
    # print(player, score)
    # input("Press Enter to continue...")

    if check_for_win(board, 'X'):
        # print('MINUS 10')
        score -= 10
        return score

    if check_for_win(board, 'O'):
        # print('PLUS 10')
        score += 10
        return score

    # if len(set(board)) == 2:
    #     score += 0
    #     return score

    branches = get_branches(board, player)

    for _, branch in branches:

        if player == 'X':
            return solve(branch, 'O', score)
        else:
            return solve(branch, 'X', score)

    return score


board = ['O', 1, 'X', 3, 'X', 5, 'O', 'X', 8]
scores = {}
player = 'O'

branches = get_branches(board, player)

print_board(board)

for branch in branches:
    print(f'Playing Spot: {branch[0]} -- {branch[1]}')
    answer = solve(branch[1], 'O', 0)
    # print(branch[0], answer)
    scores[branch[0]] = answer

print(scores)

for k, v in scores.items():
    if v == max(scores.values()):
        print(f'Checking Position: {k} for a win...')
        board[k] = 'O'
        if check_for_win(board, 'X'):
            board[k] = k
            continue
        elif check_for_win(board, 'O'):
            print(f'AI WINS!!! in position {k}')
            break
