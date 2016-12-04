import string


class Board:
    """
    Class for the board.
    It dislays the board after player defines the ships location and makes a
    move.
    """
    def __init__(self):
        self.BOARD_SIZE = 10  # sets both (x, y) to (10, 10)
        self.VERTICAL_SHIP = '|'
        self.HORIZONTAL_SHIP = '-'
        self.EMPTY = 'O'
        self.MISS = '.'
        self.HIT = '*'
        self.SUNK = '#'
        self.board = [['O' for n in range(10)] for n in range(10)]
        self.ALLOWED_CHARS = list(map(chr, range(97, (97 + self.BOARD_SIZE))))

    def clear_screen(self):
        print("\033c", end="")

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') +
                                                      self.BOARD_SIZE)]))

    def print_board(self, board):
        # prints the board on the screen
        self.print_board_heading()
        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def ship_on_board(self, ship):
        """
        This function prints out the ship as set by player

        Attributes:
        board        The board belonging to the player
        ship         The ship to be drawn information

        returns a board with the ship marked
        """
        try:
            index, orientation = self.get_index(ship)
            x_index = index[1]  # where horizontal ship starts
            y_index = index[2]  # where vertical ship starts
            if self.board[x_index][y_index] != self.EMPTY:
                raise ValueError
            else:
                h = True
                if orientation.lower() != 'y':
                    h = False
                for x in range(ship[1]):
                    if h:
                        if self.board[x_index][y_index] != self.EMPTY:
                            raise ValueError
                        else:
                            self.board[x_index][y_index] = self.HORIZONTAL_SHIP
                            y_index += 1  # draw ship horizontally
                    else:
                        if self.board[x_index][y_index] != self.EMPTY:
                            raise ValueError
                        else:
                            self.board[x_index][y_index] = self.VERTICAL_SHIP
                            x_index += 1
            return self.board
        except ValueError as e:
            print("The index {}{} is not empty".format(index[0], index[1]))
            return self.ship_on_board(ship)

    def get_index(self, ship):
        """
        Calculates the index based on input values given e.g A3.
        returns     index and orientation of ship on board
        """
        value = list(input('Place the location of the {} ({} spaces): '
                           .format(*ship)))
        # value = ['a', '2']
        orientation = input('Is it horizontal? [Y]/N: ').lower()
        # orientation = 'y'
        while True:
            if orientation not in ('y', 'n'):
                orientation = input('Is it horizontal? [Y]/N:' +
                                    '[must be y or n ] ').lower()
            else:
                break
        try:
            # make sure column headers from input are within board size
            if value[0].lower() not in self.ALLOWED_CHARS:
                raise IndexError
            # +1 because of the row numbering
            elif int(value[1]) not in range(1, self.BOARD_SIZE + 1):
                raise IndexError
            else:
                count = 0
                for char in self.ALLOWED_CHARS:
                    # convert alphabetic index to integer index
                    if value[0] is char:
                        value.append(count)
                        # -1 since lists use 0 based index
                        value[1] = int(value[1]) - 1
                        break
                    count += 1
                return (value, orientation)
        except IndexError as e:
            print('''Value you entered is not within the scope of the board.
            Should be a letter within: {}
            and a number between: {}'''
                  .format(self.ALLOWED_CHARS,
                          list(range(1, self.BOARD_SIZE + 1))))
            return self.get_index(ship)
