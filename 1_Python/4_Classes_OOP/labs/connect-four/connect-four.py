import random
from collections import deque

class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color[0].upper()

class Game:
    DEPTH = 6
    WIDTH = 8

    def __init__(self):
        self.columns = [deque(maxlen=self.DEPTH) for _ in range(self.WIDTH)]

    def place_piece(self, piece_color, columns_index):
        column = self.columns[columns_index]
        column.append(Piece(piece_color))

    def get_column(self, columns_index):
        column = self.columns[columns_index]
        out = list()

        for emptyspace in range(len(self.columns) - 1 - len(column)):
            column.append('-')
        for piece in reversed(column):
            column.append(piece)

    def print_columns(self):
        for y in reversed(range(self.DEPTH)):
            for x in range(len(self.columns) - 1):
                try:
                    print(self.columns[x][y], end=' ')
                except IndexError:
                    print('O', end=' ')
            print()

board = Game()

board.place_piece('red', 0)
board.place_piece('yellow', 0)

with open('connect-four-moves.txt', 'r') as f:
    for i, v in enumerate(f.readlines()):
        current_turn = 'yellow' if i % 2 == 0 else 'red'
        board.place_piece(current_turn, int(v) - 1)

board.print_columns()
