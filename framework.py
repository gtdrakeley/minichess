from movedecider import MoveDecider
from move import Move


class FrameworkInterface(MoveDecider):
    def __init__(self):
        super().__init__()

    def fw_move(self, string: str):
        self.move(Move.fromstr(string[0:5]))

    def fw_moves(self):
        return list(map(str, self.moves()))

    def fw_moves_shuffled(self):
        moves = self.moves_shuffled()
        return list(map(str, moves))

    def fw_moves_evaluated(self):
        mvs = self.moves_evaluated()
        return list(map(str, moves))
