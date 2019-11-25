'''
Implementation of the game: 'Fox, goose and bag of beans', aka Capra e Cavoli
Game rules could be found here: https://en.wikipedia.org/wiki/Fox,_goose_and_bag_of_beans_puzzle
'''

from .gameinterface import GameInterface
import enum

class Item(enum.Enum):
    farmer = 0
    beans = 1
    goose = 2
    fox = 3

class Game(GameInterface):
    def __init__(self):
        self.actions = list(Item)

    def reset(self):
        '''Set all items in the same side of the river'''
        self.state = {item:False for item in Item}

    def won(self):
        '''Returns true only if all the items are on the right (True) side of the river'''
        return all(self.state.values())

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
        '''String representation for the current state

        L if the item is on the left side of the river
        R if the item is on the right side of the river
        '''
        return ''.join(['R' if t else 'L' for t in self.state.values()])
