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

    def fire(self, hit_board, show_board):
        value = list(input
                     ("Enter location to hit {}: ".format(self.name).lower()))
        # value = 'd', '6'
        result = self.board.validate_play(value, hit_board, show_board)
        if result[0] == 'hit':
            print('You HIT')
            return result[1], result[2]
        elif result[0] == 'miss':
            print('You missed')
            return result[1], result[2]
        else:
            print(result[0])
            self.fire(hit_board, show_board)

# player1 = Player("dng")
# player2 = Player('john')
# player1.board = Board()
# player2.board = Board()

# player2.board.board = player1.fire(player2.board)
# player1.board.print_board(player2.board.board)
