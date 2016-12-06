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
        self.ALLOWED_NUMS = [str(s) for s in range(1, self.BOARD_SIZE + 1)]

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

    def get_index(self, ship):
        """
        Calculates the index based on input values given e.g A3.
        returns     index and orientation of ship on board
        """
        value = list(input('Place the location of the {} ({} spaces): '
                           .format(*ship)))
        # accept input with white spaces anywhere between , before
        # or after allowed input
        value = [s for s in value if s != ' ']
        orientation = input('Is it horizontal? [Y]/N: ').lower()
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
            elif value[1] not in self.ALLOWED_NUMS:
                raise IndexError
            else:
                # -1 since lists use 0 based index
                value[1] = int(value[1]) - 1
                return (value, orientation)
        except IndexError:
            print('''Value you entered is not within the scope of the board.
            Should be a letter within: {}
            and a number between: {}'''
                  .format(self.ALLOWED_CHARS,
                          self.ALLOWED_NUMS))
            return self.get_index(ship)

    def validate_index(self, index, ship, orientation):
        try:
            x_index = index[1]  # where horizontal ship starts
            y_index = self.ALLOWED_CHARS.index(index[0])  # vertical
            if self.board[x_index][y_index] != self.EMPTY:
                raise ValueError("The index {}{} is not empty"
                                 .format(self.ALLOWED_CHARS[y_index],
                                         x_index + 1))
            for x in range(ship[1]):
                if orientation:
                    if self.board[x_index][y_index] != self.EMPTY:
                        raise ValueError("The index {}{} is not empty"
                                         .format(self.ALLOWED_CHARS[y_index],
                                                 x_index + 1))
                    elif str(y_index+1) not in self.ALLOWED_NUMS:
                        # +1 since y_index is zero based for the list
                        raise IndexError("The ship will be out of the " +
                                         "board on position {}{} for " +
                                         "chosen orientation"
                                         .format(self.ALLOWED_CHARS[y_index],
                                                 x_index + 1))
                    else:
                        y_index += 1
                else:
                    if self.board[x_index][y_index] != self.EMPTY:
                        raise ValueError("The index {}{} is not empty!"
                                         .format(
                                           self.ALLOWED_CHARS[y_index],
                                           x_index + 1))
                    elif str(x_index) not in self.ALLOWED_NUMS:
                        # +1 since y_index is zero based for the list
                        raise IndexError("The ship will be out of the " +
                                         "board on position {}{} for " +
                                         "chosen orientation"
                                         .format(
                                          self.ALLOWED_CHARS[y_index],
                                          x_index + 1))
                    else:
                        x_index += 1
        except ValueError as e:
            print(e.args[0])
            return False
        except IndexError as e:
            print(e.args[0])
            return False
        else:
            return True

    def ship_on_board(self, ship):
        """
        This function prints out the ship as set by player

        Attributes:
        board        The board belonging to the player
        ship         The ship to be drawn information

        returns a board with the ship marked
        """
        index, orientation = self.get_index(ship)
        x_index = index[1]  # where horizontal ship starts
        y_index = self.ALLOWED_CHARS.index(index[0])
        h = True
        if orientation.lower() != 'y':
            h = False
        if self.validate_index(index, ship, h):
            for x in range(ship[1]):
                if h:
                    self.board[x_index][y_index] = self.HORIZONTAL_SHIP
                    y_index += 1  # draw ship horizontally
                else:
                    self.board[x_index][y_index] = self.VERTICAL_SHIP
                    x_index += 1  # draw ship vertically
            return self.board
        else:
            self.ship_on_board(ship)

# b = Board()
# ships = [
#     ("Aircraft Carrier", 5),
#     ("Patrol Boat", 2)
# ]

# for ship in ships:
#     b.ship_on_board(ship)
#     b.print_board(b.board)
