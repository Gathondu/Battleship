from board import Board
from player import Player
from ship import Ship


if __name__ == "__main__":
    default_board = Board().board
    player_board = Board()
    ships = Ship()
    index = 0
    orientation = 'y'
    # player1 = Player(input('Enter your name: '), Ship.get_ships())

    def clear_screen():
        print("\033c", end="")

    # Place the location of the aircraft carrier (5 spaces): a2
    # Is it horizontal? (Y)/N: n
    def get_player_ships():
        try:
            for ship in ships.get_ships():
                get_index(ship)
                player_board.ship_board(player_board.board, ship, index,
                                        orientation)
        except:
            raise

    get_player_ships()
    # h = True
    # index = range(3)
    # for x in index:
    #     if h:
    #         board[x] = '.' + 'O' * 9
    #     else:
    #         board[0][x] = '.'
    # print_board(board)
