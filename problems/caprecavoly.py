"""
Implementation of the game: 'Fox, goose and bag of beans', aka Capra e Cavoli
Game rules could be found here: https://en.wikipedia.org/wiki/Fox,_goose_and_bag_of_beans_puzzle
"""

from .gameinterface import GameInterface
from enum import Enum

class Item(Enum):
    farmer = 0
    beans = 1
    goose = 2
    fox = 3

class Game(GameInterface):
    def __init__(self):
        self.actions = [ item for item in Item ]

    def reset(self):
        self.state = { item:False for item in Item }

    def won(self):
        return all([side for side in self.state.values()])

    def lost(self):
        farmer_side = self.state[Item.farmer]
        opp_side = [item for item, side in self.state.items() if side != farmer_side]

        collision = (
                (Item.goose in opp_side and Item.beans in opp_side)
            or
            (Item.goose in opp_side and Item.fox in opp_side)
        )
        return collision

    def do_action(self, action):
        # farmer changes river side
        self.state[Item.farmer] = not self.state[Item.farmer]

        # Other thing changes river side
        if action != Item.farmer:
            self.state[action] = not self.state[action]

    def get_actions(self):
        return self.actions

    def get_state(self):
        return ''.join(['L' if t else 'R' for t in self.state.values()])
