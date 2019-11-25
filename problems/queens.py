from .gameinterface import GameInterface
from collections import namedtuple

Coord = namedtuple('Coord', ('x', 'y'))

def conflict(queen1, queen2):
    if queen1.x == queen2.x or queen1.y == queen2.y:
        # Same - or |
        return True

    if queen1.x + queen1.y == queen2.x + queen2.y:
        # Same / diagonal
        return True

    if queen1.x - queen1.y == queen2.x - queen2.y:
        # Same \ diagonal
        return True
    return False


class Game(GameInterface):
    def __init__(self):
        # NOTE: this game is very hard to learn attempts should be ~ 3*10^4
        self.attempts = 3*(10**4)
        self.possible_actions = [0, 1, 2, 3, 4, 5, 6, 7]

    def reset(self):
        self.state = []

    def lost(self):
        for q1x, q1y in enumerate(self.state):
            for q2d, q2y in enumerate(self.state[q1x+1:]):
                q2x = q1x + q2d +1
                if conflict(Coord(q1x, q1y), Coord(q2x, q2y)):
                    return True
        return False

    def won(self):
        return len(self.state) == 8 and not self.lost()

    def get_actions(self):
        return self.possible_actions

    def do_action(self, column):
        self.state.append(column)

    def get_state(self):
        return str(self.state)
