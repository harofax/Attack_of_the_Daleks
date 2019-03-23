class GameBoard:
    """
    Attributes:
    board:      the array containing the game-board
    tiles:      a dictionary containing the characters for the tiles/entities
    entities:   a list of all the entities in the map
    """

    def __init__(self, board_file):
        """
        Creates a new GameBoard from a text file and populates the
        board-array as well as the entities list.
        :param board_file: a .txt file containing the board layout
        """

        try:
            self.board = self.parse_board(board_file)
        except FileNotFoundError as fnf:
            print("The file %s does not exist!" % fnf.filename)

    def __str__(self):
        """
        The board in string form, can be used for printing the stage
        :return:
        """

    def get_creature_at(self, x, y):
        """
        Gets the creature located at the given x and y coordinates
        :param x:   x-coordinate
        :param y:   y-coordinate
        :return:    returns the Entity gotten, or None if no creature was found.
        """

    def get_tile_at(self, x, y):
        """
        Get's the tile at the given x and y coordinates
        :param x:   x-coordinate
        :param y:   y-coordinate
        :return:    Tile object
        """

    def parse_board(self, board_file):
        """
        A function to parse a text-file containing the board and
        populating the board-array with it
        :param board_file:     text file containing the board layout
        :return:               2 dimensional array containing the tiles from the board file
        """
        with open(board_file) as file:
            for
                """#########################################################
                ################## CONTINUE HERE ###########################
                #########################################################"""


class Tile:
    """
    A tile on the map, either a floor ".", or a wall "#".
    Attributes:
    tile:     the character representing the tile
    """
    def __init__(self, tile):
        """
        Creates a new tile
        :param tile: the character of the tile - either a # or a . depending on tile type
        """

    def isWall(self):
        """
        Checks if the tile is a wall tile
        :return: Boolean variable, true if self.tile == "#"
        """

