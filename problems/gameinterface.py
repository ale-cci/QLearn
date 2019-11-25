import abc

class GameInterface:
    attempts = 100

    @abc.abstractmethod
    def reset(self):
        ''' When called the game should be resetted at the initial condition '''
        pass

    @abc.abstractmethod
    def won(self) -> bool:
        ''' Method called to check if the '''
        pass

    @abc.abstractmethod
    def lost(self) -> bool:
        ''' Returns True if the player has lost in the given game state '''
        pass

    @abc.abstractmethod
    def do_action(self, encoded_action) -> None:
        ''' Execute the current player action '''
        pass

    @abc.abstractmethod
    def get_actions(self) -> list:
        ''' Get the possible actions that the player can do '''
        pass

    def draw(self) -> None:
        ''' Render the current game state '''
        pass

    @abc.abstractmethod
    def get_state(self):
        ''' Returns an unique codification of the current game state '''
        pass
