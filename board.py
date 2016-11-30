import string

class Board:
    """
    Class for the board.
    It dislays the board after player defines the ships location and makes a
    move.
    """
    BOARD_SIZE = 10  # default board size and sets both (x, y) to (10, 10)
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    board = [['O' for n in range(10)] for n in range(10)]

    def clear_screen():
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

    def ship_on_board(self, board, ship):
        """
        This function prints out the ship as set by player

        Attributes:
        board        The board belonging to the player
        ship         The ship to be drawn information

        returns a board with the ship marked
        """
        index, orientation = self.get_index(ship)
        x_index = index[1]  # where horizontal ship starts
        y_index = index[0]  # where vertical ship starts
        h = True
        if orientation.lower() != 'y':
            h = False
        for x in range(ship_info[1]):
            if h:
                board[x_index][y_index] = self.HORIZONTAL_SHIP
                y_index += 1  # draw ship horizontally
            else:
                board[x_index][y_index] = self.VERTICAL_SHIP
                x_index += 1
        return board

    def get_index(self, ship):
        """
        Calculates the index based on input values given e.g A3.
        returns     index and orientation of ship on board
        """
        value = list(raw_input('Place the location of the {} ({} spaces): '
                    .format(*ship)))
        value[0] = value[0].lower()
        orientation = raw_input('Is it horizontal? [Y]/N: ').lower()
        while true:
            if orientation not in ('y', 'n'):
                orientation = raw_input('Is it horizontal? [Y]/N:[must be y or n ] ').lower()
            else:
                break
        try:
            if value[0] not in list(map(chr, range(97, (97+ self.BOARD_SIZE)))):  # make sure column headers from input are within board size
                raise IndexError
            elif value[1] not in range(self.BOARD_SIZE+1):  # +1 because of the row numbering
                raise IndexError
            else:
                count = 1
                for char in list(map(chr, range(97, (97+ self.BOARD_SIZE)))):  # convert alphabetic index to integer index
                    if value[0] is char:
                        value[0] = count
                        break
                    count +=1
            return (value,orientation)
        except IndexError as e:
            print('''Value you entered is not within the scope of the board. Should be a letter within: {}
                    and a number between: {}'''.format(list(map(chr, range(97, (97+ self.BOARD_SIZE)))), list(range(self.BOARD_SIZE)))
            (value, orientation) = get_index(self.ship)
