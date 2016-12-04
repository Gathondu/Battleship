from board import Board
from player import Player
from ship import Ship

if __name__ == "__main__":
    default = Board()
    NO_OF_PLAYERS = 2
    ships = Ship()
    player1 = Player(input('Enter your name player 1: '))
    default.clear_screen()
    player2 = Player(input('Enter your name player 2: '))
    player1.board = Board()
    player2.board = Board()
    default.clear_screen()
    print(player1.name.upper() + ':')
    player1.get_player_ships(player1.board, [("Aircraft", 5),
                                             ("Submarine", 4)])
    default.clear_screen()
    player1.board.print_board(player1.board.board)
    input('Hit enter to continue')
    default.clear_screen()
    print(player2.name.upper() + ':')
    player2.get_player_ships(player2.board, [("Aircraft", 5),
                                             ("Submarine", 4)])
    player2.board.print_board(player2.board.board)
    input('Hit enter to continue')
    default.clear_screen()
