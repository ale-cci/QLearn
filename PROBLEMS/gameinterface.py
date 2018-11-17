
class GameInterface:
    def reset(self):
        """ When called the game should be resetted at the initial condition """
        raise NotImplementedError()

    def won(self) -> bool:
        """ Method called to check if the """
        raise NotImplementedError()

    def lost(self) -> bool:
        """ Returns True if the player has lost in the given game status """
        raise NotImplementedError()

    def do_action(self, encoded_action) -> None:
        """ Execute the current player action """
        raise NotImplementedError()

    def get_actions(self) -> list:
        """ Get the possible actions that the player can do """
        raise NotImplementedError()

    def draw(self) -> None:
        pass
    
    def get_status(self):
        """ Returns an unique codification of the current game status """
        raise NotImplementedError()
