'''
Implementation of the eight queens puzzle
https://en.wikipedia.org/wiki/Eight_queens_puzzle
'''
from collections import namedtuple
from problems.gameinterface import GameInterface

Coord = namedtuple('Coord', ('x', 'y'))

def conflict(queen1, queen2):
    ''' Check if the two queens are in the same line '''
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
    '''8 Queens'''
    def __init__(self):
        # Row where a queen could be placed
        self.possible_actions = [0, 1, 2, 3, 4, 5, 6, 7]

        # NOTE: this game is very hard to learn attempts should be ~ 3*10^4
        self.attempts = 3*(10**4)

        # State initialized by reset
        self.state = None

    def reset(self):
        ''' Remove all queens from the chessboard '''
        self.state = []

    def lost(self):
        ''' Check if a pair of queens are in the same line '''

        for q1x, q1y in enumerate(self.state):
            for q2d, q2y in enumerate(self.state[q1x+1:]):
                q2x = q1x + q2d +1
                if conflict(Coord(q1x, q1y), Coord(q2x, q2y)):
                    return True
        return False

    def won(self):
        '''
        Win condition if all queens are placed and there's no conflict
        '''
        return len(self.state) == 8 and not self.lost()

    def get_actions(self):
        '''Straight return the list of actions'''
        return self.possible_actions

    def do_action(self, encoded_action):
        '''Add the queen in the chessboard in the specified column'''
        self.state.append(encoded_action)

    def get_state(self):
        '''Return list of placed queens'''
        return str(self.state)
