# Game Rules:

possible_actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]   # Top Down Left Right
initial_status = (0, 0)                 # Start position

_hidden_obstacles = [
]

_game_w = 5
_game_h = 5

def won(status):
        return status == (_game_w, _game_h)

def lost(status):
        return status in _hidden_obstacles

def next_status(status, action):
        dx, dy = possible_actions[action]
        x, y = status

        # Bounding new Coords
        x0 = min(max(0, x+dx), _game_w)
        y0 = min(max(0, y+dy), _game_h)
        return x0, y0

from PROBLEMS.game import GameInterface
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

    def encoded_status(self):
        return str(self._position)
