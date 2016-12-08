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
        self.ALL_CHARS = list(map(chr, range(97, 123)))
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
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def get_index(self, value):
        """
        Calculates the index based on input values given e.g A3.
        returns     index and bool value indicating no errors
        """
        try:
            # accept input with white spaces anywhere between , before
            # or after allowed input
            value = [s for s in value if s != ' ']

            # check if there was a double digit input
            if len(value) > 2:
                digits = [s for s in value if s.isdigit()]
                digits = "".join(digits)
                value[1] = digits
                value.pop()
            elif len(value) > 3:
                raise IndexError('Value you entered is not within the scope of'
                                 ' the board. Should be a letter within: \n{}'
                                 '\n and a number between: \n{}'
                                 .format(self.ALLOWED_CHARS,
                                         self.ALLOWED_NUMS))

            # make sure column headers from input are within board size
            if value[0].lower() not in self.ALLOWED_CHARS:
                raise IndexError('Value you entered is not within the scope of'
                                 ' the board. Should be a letter within: \n{}'
                                 '\n and a number between: \n{}'
                                 .format(self.ALLOWED_CHARS,
                                         self.ALLOWED_NUMS))
            elif value[1] not in self.ALLOWED_NUMS:
                raise IndexError('Value you entered is not within the scope of'
                                 ' the board. Should be a letter within: \n{}'
                                 '\n and a number between: \n{}'
                                 .format(self.ALLOWED_CHARS,
                                         self.ALLOWED_NUMS))
            else:
                # -1 since lists use 0 based index
                value[1] = int(value[1]) - 1
                return (value, True)
        except IndexError as i:
            self.clear_screen()
            self.print_board(self.board)
            print(i.args[0])
            return (value, False)

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
                    if y_index not in range(10):
                        # +1 since y_index is zero based for the list
                        raise IndexError('The ship will be out of the'
                                         ' board on position {}{} for chosen'
                                         ' orientation'.format
                                         (self.ALL_CHARS[y_index],
                                          x_index + 1))
                    elif self.board[x_index][y_index] != self.EMPTY:
                        raise ValueError("The index {}{} is not empty"
                                         .format(self.ALLOWED_CHARS[y_index],
                                                 x_index + 1))
                    else:
                        y_index += 1
                else:
                    if x_index not in range(10):
                        raise IndexError('The ship will be out of the'
                                         ' board on position {}{} for'
                                         ' chosen orientation'.format
                                         (self.ALL_CHARS[y_index],
                                          x_index + 1))
                    elif self.board[x_index][y_index] != self.EMPTY:
                        raise ValueError("The index {}{} is not empty!"
                                         .format(
                                           self.ALLOWED_CHARS[y_index],
                                           x_index + 1))
                    else:
                        x_index += 1
        except ValueError as e:
            self.clear_screen()
            self.print_board(self.board)
            print(e.args[0])
            return False
        except IndexError as i:
            self.clear_screen()
            self.print_board(self.board)
            print(i.args[0])
            return False
        else:
            return True

    def validate_play(self, index, board):
        try:
            x_index = int(index[1]) - 1  # where horizontal ship starts
            y_index = self.ALLOWED_CHARS.index(index[0])  # vertical
            if y_index not in range(10) or x_index not in range(10):
                # +1 since y_index is zero based for the list
                raise IndexError('The position {}{} will be out of the'
                                 ' board!!'
                                 .format(self.ALL_CHARS[y_index],
                                         x_index + 1))
            elif board[x_index][y_index] == self.EMPTY:
                board[x_index][y_index] = self.MISS
                return board, "miss"
            elif board[x_index][y_index] == self.VERTICAL_SHIP:
                board[x_index][y_index] = self.HIT
                return board, "hit"
            elif board[x_index][y_index] == self.HORIZONTAL_SHIP:
                board[x_index][y_index] = self.HIT
                return board, "hit"
            elif board[x_index][y_index] == self.MISS:
                raise ValueError('You cannot play that position again.'
                                 ' You already played it!')
            elif board[x_index][y_index] == self.HIT:
                raise ValueError('You cannot play that position again.'
                                 ' You already played it!')
        except IndexError as i:
            self.clear_screen()
            return board, i.args[0]
        except ValueError as e:
            self.clear_screen()
            return board, e.args[0]

    def ship_on_board(self, ship):
        """
        This function prints out the ship as set by player

        Attributes:
        board        The board belonging to the player
        ship         The ship to be drawn information

        returns a board with the ship marked
        """
        value = list(input('Place the location of the {} ({} spaces): '
                           .format(*ship)).lower())
        orientation = input('Is it horizontal? [Y]/N: ').lower()
        # value = ['d', '6']
        # orientation = 'y'
        while True:
            if orientation not in ('y', 'n'):
                self.clear_screen()
                self.print_board(self.board)
                orientation = input('Is it horizontal? [Y]/N:' +
                                    '[must be y or n ] ').lower()
            else:
                break
        index = self.get_index(value)  # returns a tuple
        if index[1]:
            x_index = index[0][1]  # where horizontal ship starts
            y_index = self.ALLOWED_CHARS.index(index[0][0])
            h = True
            if orientation.lower() != 'y':
                h = False
            if self.validate_index(index[0], ship, h):
                for x in range(ship[1]):
                    if h:
                        self.board[x_index][y_index] = self.HORIZONTAL_SHIP
                        y_index += 1  # draw ship horizontally
                    else:
                        self.board[x_index][y_index] = self.VERTICAL_SHIP
                        x_index += 1  # draw ship vertically
                self.clear_screen()
                return self.board
            else:
                self.ship_on_board(ship)
        else:
            self.ship_on_board(ship)


# b = Board()
# # ships = [
# #     ("Aircraft Carrier", 5),
# #     ("Patrol Boat", 2)
# #

# # for ship in ships:
# #     b.ship_on_board(ship)
# #     b.print_board(b.board)
# b.validate_play(('d', '8'), b.board)
# b.print_board(b.board)
