from Tile import *
from Dalek import *
from Scrap import *
from Doctor import *


class GameBoard:
    """
    Attributes:
    board:      the array containing the game-board
    entities:   a list of all the entities in the map
    """

    def __init__(self, board_file):
        """
        Creates a new GameBoard from a text file and populates the
        board-array as well as the entities list.
        :param board_file: a .txt file containing the board layout
        """
        self.entities = []
        try:
            self.board = self.parse_board(board_file)
        except FileNotFoundError as fnf:
            print("The file %s does not exist!" % fnf.filename)

    def __str__(self):
        """
        The board in string form, can be used for printing the stage
        :return:
        """
        board_string = ""
        for row in self.board:
            board_string += "".join([str(cell) for cell in row])
            board_string += '\n'

        return board_string

    def get_entity_at(self, x, y):
        """
        Gets the Entity located at the given x and y coordinates
        :param x:   x-coordinate
        :param y:   y-coordinate
        :return:    returns the Entity gotten, or None if no creature was found.
        """
        if isinstance(self.board[y][x], Entity):
            return self.board[y][x]
        else:
            return None

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

        # Load all the data into the array
        with open(board_file) as file:
            board = [list(line.strip('\n')) for line in file]

        # Replace characters with tiles and put entities into lists
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == ".":
                    board[y][x] = Tile(".")
                elif board[y][x] == "#":
                    board[y][x] = Tile("#")
                elif board[y][x] == "D":
                    dalek = Dalek(x, y)
                    board[y][x] = dalek
                    self.entities.append(dalek)
                elif board[y][x] == "W":
                    doctor = Doctor(x, y)
                    board[y][x] = doctor
                    self.entities.append(doctor)

        return board






