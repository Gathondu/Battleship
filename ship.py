class Ship:
    """
    Contains the ships used in the game
    """
    name = 'Ship'
    size = 0

    SHIP_INFO = [  # information about the ships in the class
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]

    def get_ships(self):
        return self.SHIP_INFO


class Aircraft(Ship):
    def __init__(self):
        self.name = 'Aircraft Carrier'
        self.size = 5


class Battleship(Ship):
    def __init__(self):
        self.name = 'Battleship'
        self.size = 4


class Submarine(Ship):
    def __init__(self):
        self.name = 'Submarine'
        self.size = 3


class Cruiser(Ship):
    def __init__(self):
        self.name = 'Cruiser'
        self.size = 3


class Patrol(Ship):
    def __init__(self):
        self.name = 'Patrol Boat'
        self.size = 2
