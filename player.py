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
        value = list(input
                     ("Enter location to hit {}: ".format(self.name).lower()))
        # value = 'd', '6'
        result = self.board.validate_play(value, board)
        return result

# player1 = Player("dng")
# player2 = Player('john')
# player1.board = Board()
# player2.board = Board()

# player2.board.board = player1.fire(player2.board)
# player1.board.print_board(player2.board.board)
