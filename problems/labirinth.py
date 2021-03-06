'''
Trivial labirinth puzzle
'''
from collections import namedtuple
from problems.gameinterface import GameInterface

Coord = namedtuple('Coord', ('x', 'y'))

def bound(value, low, high):
    '''Bound value between low and high values'''
    return min(max(low, value), high)

class Game(GameInterface):
    '''
    The Labirinth puzzle

    :board: is the size of the labirinth
    :_hidden_obstacles: is a list of Coords.
        If the player touches an obstacle, the game is considered lost
    :actions: single step in a direction (North, South, West, East)
    :_goal: coordinate that the player should reach to win the game
    :_initial_position: The initial position of the player
    :_position: Current position of the player

    '''

    def __init__(self):
        '''
        Initialize this labirinth

        #######
        #P....#
        #xx...#
        #.....#
        #...xx#
        #....@#
        #######

        :P: is the player initial position
        :@: is the goal
        :x: is a wall (hidden obstacle)
        :.: is a path

        '''
        self._hidden_obstacles = [
            Coord(x=0, y=1),
            Coord(x=1, y=1),
            Coord(x=3, y=3),
            Coord(x=4, y=3),
        ]

        self.actions = [
            Coord(0, -1),
            Coord(0, +1),
            Coord(-1, 0),
            Coord(+1, 0)
        ]

        self.board = Coord(5, 5)
        self._goal = Coord(4, 4)
        self._initial_position = Coord(0, 0)

        self._position = None


    def reset(self):
        '''Move player in the starting position'''
        self._position = self._initial_position

    def do_action(self, encoded_action):
        '''Update player coordinates based on the action taken'''
        pos_x, pos_y = self._position

        self._position = Coord(
            bound(pos_x + encoded_action.x, low=0, high=self.board.x),
            bound(pos_y + encoded_action.y, low=0, high=self.board.y)
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
