"""
    Implementation of the game: 'Fox, goose and bag of beans', aka Capra e Cavoli
    Game rules could be found here: https://en.wikipedia.org/wiki/Fox,_goose_and_bag_of_beans_puzzle
"""
from PROBLEMS.game import GameInterface

class Game(GameInterface):
    def reset(self):
        self.status = [False]*4
        self.actions = [0, 1, 2, 3]

    def won(self):
        return not (False in self.status)

    def lost(self):
        tmp = [s != self.status[0] for s in self.status]
        return tmp[2] and (tmp[1] or tmp[3])

    def do_action(self, action):
        # farmer changes river side
        self.status[0] = not self.status[0]

        # Other thing changes river side
        if action != 0:
            self.status[action] = not self.status[action]

    def get_actions(self):
        return self.actions

    def encoded_status(self):
        return ''.join(['L' if t else 'R' for t in self.status])
