import os
import random


class Game:
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

        # player 'X' goes first
        self.player_turn = 'X'

    # updated board printer
    def print_board(self):
        print('+---+---+---+')
        for line in range(3):
            # get each block in current line
            block_0 = self.board[line][0]
            block_1 = self.board[line][1]
            block_2 = self.board[line][2]
            # check if block is empty, if so display spot number for play
            if block_0 == ' ':
                block_0 = (line * 3) + 1
            if block_1 == ' ':
                block_1 = (line * 3) + 2
            if block_2 == ' ':
                block_2 = (line * 3) + 3
            # print out the board
            print(
                f'| {block_0} | {block_1} | {block_2} |')
            print('+---+---+---+')
        print()

    # displays game results and winner if not scratch/draw.
    def game_over(self, winner):
        # self.print_board()
        if winner == 'SCRATCH':
            print(f'Game Over! It\'s a SCRATCH!!!')
        else:
            print(f'Game Over! {winner} WINS!!!')

    # check to see if the chosen position is valid
    def is_valid(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        elif self.board[x][y] != ' ':
            return False
        else:
            return True

    def is_end(self):  # check to see if the game has been won/scratched
        # vertical win
        for column in range(3):
            if (self.board[0][column] != ' ' and
                self.board[0][column] == self.board[1][column] and
                    self.board[1][column] == self.board[2][column]):
                return self.board[0][column]

        # horizontal win
        for line in range(3):
            if (self.board[line] == ['X', 'X', 'X']):
                return 'X'
            elif (self.board[line] == ['O', 'O', 'O']):
                return 'O'

        # top-left to bottom-right diagonal win
        if (self.board[0][0] != ' ' and
            self.board[0][0] == self.board[1][1] and
                self.board[0][0] == self.board[2][2]):
            return self.board[0][0]

        # top-right to bottom-left  diagonal win
        if (self.board[0][2] != ' ' and
            self.board[0][2] == self.board[1][1] and
                self.board[0][2] == self.board[2][0]):
            return self.board[0][2]

        # check if board if complete
        for line in range(3):
            for column in range(3):
                if (self.board[line][column] == ' '):
                    return None

        return ' '  # game is a scratch

    def pick_random(self):
        open_positions = []
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == ' ':
                    open_positions.append((row, column))
        return open_positions

    def max(self):  # player 'O' is the computer player
        max_value = -2
        x = None
        y = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)  # loss
        elif result == 'O':
            return (1, 0, 0)  # win
        elif result == ' ':
            return (0, 0, 0)  # tie

        for row in range(3):
            for column in range(3):
                if self.board[row][column] == ' ':
                    self.board[row][column] = 'O'
                    (score, min_row, min_column) = self.min()
                    if score > max_value:
                        max_value = score
                        x = row
                        y = column
                    self.board[row][column] = ' '
        return (max_value, x, y)

    def min(self):  # player 'X' is the human player
        min_value = 2
        x2 = None
        y2 = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == ' ':
            return (0, 0, 0)

        for row in range(3):
            for column in range(3):
                if self.board[row][column] == ' ':
                    self.board[row][column] = 'X'
                    (score, max_row, max_column) = self.max()
                    if score < min_value:
                        min_value = score
                        x2 = row
                        y2 = column
                    self.board[row][column] = ' '

        return (min_value, x2, y2)

    def play(self):  # time to play the game

        while True:

            self.result = self.is_end()

            # if game is over display end screen
            if self.result != None:
                if self.result == 'X':
                    # self.game_over('X')
                    return 'X'
                elif self.result == 'O':
                    # self.game_over('O')
                    return 'O'
                elif self.result == ' ':
                    # self.game_over('SCRATCH')
                    return 'TIE'

                self.start_game()
                return

            # if human player, ask for move
            if self.player_turn == 'X':
                options = self.pick_random()
                ran = random.randint(0, len(options) - 1)
                playing = options[ran]

                self.board[playing[0]][playing[1]] = 'X'

                # (score, x, y) = self.min()
                # self.board[x][y] = 'X'

                self.player_turn = 'O'
            else:
                # options = self.pick_random()
                # ran = random.randint(0, len(options) - 1)
                # playing = options[ran]

                # self.board[playing[0]][playing[1]] = 'O'

                (score, x, y) = self.max()
                self.board[x][y] = 'O'

                self.player_turn = 'X'


def main():
    stats = {'X': 0, 'O': 0, 'TIE': 0}
    for i in range(1000):
        g = Game()
        stats[g.play()] += 1

    print(stats)


if __name__ == "__main__":
    main()
