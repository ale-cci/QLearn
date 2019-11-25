import abc

class GameInterface:
    '''Game interface specifies all actions required by the Q-Learning algorithm'''

    attempts = 100

    @abc.abstractmethod
    def reset(self):
        '''When called the game should be resetted at the initial condition'''

    @abc.abstractmethod
    def won(self) -> bool:
        '''Should return True if the game has ended in a winning state'''

    @abc.abstractmethod
    def lost(self) -> bool:
        '''Should return True if the game has ended in a losing state'''

    @abc.abstractmethod
    def do_action(self, encoded_action) -> None:
        '''Execute the current player action'''

    @abc.abstractmethod
    def get_actions(self) -> list:
        '''Get the possible actions that the player can do'''

    def draw(self) -> None:
        '''Render the current game state'''

    @abc.abstractmethod
    def get_state(self):
        '''Returns an unique codification of the current game state'''
