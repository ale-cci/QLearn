from PROBLEMS.gameinterface import GameInterface
from collections import namedtuple

def bound(value, minimum, maximum):
    return min(max(minimum, value), maximum)

class Game(GameInterface):
    def __init__(self):
        self._hidden_obstacles = []

        Coordinates = namedtuple('Coordinates', ('x', 'y'))
        self.actions = [
            Coordinates(0, -1),
            Coordinates(0, +1),
            Coordinates(-1, 0),
            Coordinates(+1, 0)
        ]

        self.board = Coordinates(5, 5)

        self._goal = [4, 4]

    def reset(self):
        self._position = [0, 0]

    def do_action(self, action):
        self._position[0] = bound(self._position[0] + action.x, minimum=0, maximum=self.board.x)
        self._position[1] = bound(self._position[1] + action.y, minimum=0, maximum=self.board.y)


    def lost(self):
        return self._position in self._hidden_obstacles

    def won(self):
        return self._position == self._goal

    def get_actions(self) -> list:
        return self.actions

    def get_status(self):
        return str(self._position)
