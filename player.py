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
                board.print_board(board.board)

    def fire(self, board):
        value = list(input("Enter location to hit: "))
        result = board.validate_play(value, board.board)
        board.board = result[0]
        return result[0]
