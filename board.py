from move import Move
from typing import List


class Board:
    def __init__(self) -> None:
        self.turn = 1  # type: int
        self.playing = 'W'  # type: str
        self.board = list([list('kqbnr'),  # type: List[List[str]]
                           list('ppppp'),
                           list('.....'),
                           list('.....'),
                           list('PPPPP'),
                           list('RNBQK')])

    def reset(self) -> None:
        self.__init__()

    def get_board(self) -> str:
        return '{} {}\n{}\n'.format(self.turn, self.playing, map(''.join, self.board))

    def set_board(self, board_string: str) -> None:
        turn_state, *board_state = board_string.split('\n')
        turn, playing = turn_state.split()
        self.turn, self.playing = int(turn), playing
        self.board = list(map(list, board_state))

    def winner(self) -> str:
        board = ''.join(map(''.join, self.board))
        if 'K' in board and 'k' not in board:
            return 'W'
        elif 'K' not in board and 'k' in board:
            return 'B'
        elif self.turn > 40:
            return '='
        else:
            return '?'

    def move(self, mv: Move) -> None:
        if self.playing == 'W':
            self.playing = 'B'
        else:
            self.playing = 'W'
            self.turn += 1
        src_piece = self.board[mv.src_row][mv.src_column]
        self.board[mv.src_row][mv.src_column] = '.'
        if src_piece == 'P' and mv.dest_row == 0:
            self.board[mv.dest_row][mv.dest_column] = 'Q'
        elif src_piece == 'p' and mv.dest_row == 5:
            self.board[mv.dest_row][mv.dest_column] = 'q'
        else:
            self.board[mv.dest_row][mv.dest_column] = src_piece