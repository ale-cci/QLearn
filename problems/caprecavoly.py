'''
Implementation of the game: 'Fox, goose and bag of beans', aka Capra e Cavoli
Game rules could be found here: https://en.wikipedia.org/wiki/Fox,_goose_and_bag_of_beans_puzzle
'''

import enum

from problems.gameinterface import GameInterface

class Item(enum.Enum):
    '''
    Enumeration of entities in the game,
    with their respective string representation
    '''

    Farmer = "👨"
    Beans = "🥫"
    Goose = "🦆"
    Fox = "🦊"

class Game(GameInterface):
    '''
    Fox, Goose and Bag of Beans
    '''
    def __init__(self):
        self.actions = list(Item)

        # Field initialized dynamically by reset
        self.state = None

    def reset(self):
        '''Set all items in the same side of the river'''
        self.state = {item:False for item in Item}

    def won(self):
        '''Returns true only if all the items are on the right (True) side of the river'''
        return all(self.state.values())

    def lost(self):
        farmer_side = self.state[Item.Farmer]
        opp_side = [item for item, side in self.state.items() if side != farmer_side]

        collision = (
            (Item.Goose in opp_side and Item.Beans in opp_side)
            or
            (Item.Goose in opp_side and Item.Fox in opp_side)
        )
        return collision

    def do_action(self, encoded_action):
        # farmer changes river side
        self.state[Item.Farmer] = not self.state[Item.Farmer]

        # Other thing changes river side
        if encoded_action != Item.Farmer:
            self.state[encoded_action] = not self.state[encoded_action]

    def get_actions(self):
        return self.actions

    def draw(self):
        print(
                [item.value if not self.state[item] else '  ' for item in Item],
                '~',
                [item.value if self.state[item] else '  ' for item in Item]
            )


    def get_state(self):
        '''String representation for the current state

        L if the item is on the left side of the river
        R if the item is on the right side of the river
        '''
        return ''.join(['R' if t else 'L' for t in self.state.values()])
