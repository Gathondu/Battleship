from board import Board
from player import Player
from ship import Ship

if __name__ == "__main__":
    ships = Ship()
    NO_OF_PLAYERS = 2
    default = Board()

    default.clear_screen()
    player1 = Player(input('Enter your name player 1: '))
    player2 = Player(input('Enter your name player 2: '))
    # player1 = Player('dng')
    # player2 = Player('john')
    player1.board = Board()
    player1.show_board = Board().board
    player2.board = Board()
    player2.show_board = Board().board
    default.print_board(default.board)
    input('This is how the game board board looks like. Hit enter to continue')
    default.clear_screen()
    default.print_board(default.board)
    print(player1.name.upper() + ':')
    player1.get_player_ships(player1.board, [("Aircraft", 5)])
    default.clear_screen()
    player1.board.print_board(player1.board.board)
    input('Hit enter to continue')
    default.clear_screen()
    default.print_board(default.board)
    print(player2.name.upper() + ':')
    player2.get_player_ships(player2.board, [("Aircraft", 5)])
    default.clear_screen()
    player2.board.print_board(player2.board.board)
    input('Hit enter to continue')
    default.clear_screen()

    count = 0
    while True:
        if count == 0:
            count = 1
            default.clear_screen()
            default.print_board(default.board)
            result = player1.fire(player2.board.board, player1.show_board)
            player2.board.board = result[0]
            player1.show_board = result[1]
            player1.board.print_two_boards
            ((player1.board.board, player1.show_board))
        else:
            count = 0
            default.clear_screen()
            default.print_board(default.board)
            result = player2.fire(player1.board.board, player2.show_board)
            player1.board.board = result[0]
            player2.show_board = result[1]
            player2.board.print_two_boards
            ((player2.board.board, player1.show_board))
