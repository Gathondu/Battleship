from board import Board


class Player:
    """
    Sets player name, ships available to the player and their orientation
    """

    def __init__(self, name):
        # initialize a player with a name
        self.name = name

    def get_player_ships(self, board, ships):
            for ship in ships:
                board.ship_on_board(ship)
