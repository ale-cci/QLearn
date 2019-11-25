from collections import namedtuple
from .gameinterface import GameInterface

Coordinate = namedtuple('Coordinate', ('x', 'y'))

def bound(value, low, high):
    '''Bound value between low and high values'''
    return min(max(low, value), high)

class Game(GameInterface):
    def __init__(self):
        self._hidden_obstacles = []

        self.actions = [
            Coordinate(0, -1),
            Coordinate(0, +1),
            Coordinate(-1, 0),
            Coordinate(+1, 0)
        ]

        self.board = Coordinate(5, 5)

        self._goal = Coordinate(4, 4)

    def reset(self):
        self._position = Coordinate(0, 0)

    def do_action(self, action):
        '''Update player coordinates based on the action taken'''
        pos_x, pos_y = self._position

        self._position = Coordinate(
            bound(pos_x + action.x, low=0, high=self.board.x),
            bound(pos_y + action.y, low=0, high=self.board.y)
        )


    def lost(self):
        '''Lose the game if agent hits an obstacle'''
        return self._position in self._hidden_obstacles

    def won(self):
        return self._position == self._goal

    def get_actions(self) -> list:
        return self.actions

    def get_state(self):
        return str(self._position)
