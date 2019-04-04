import Dalek
import Doctor
from Tile import *


class GameBoard:
    """
    Attributes:
    board:      the array containing the game-board
    entities:   a list of all the entities in the map
    player:     the player
    """

    def __init__(self, board_file):
        """
        Creates a new GameBoard from a text file and populates the
        board-array as well as the entities list.
        :param board_file: a .txt file containing the board layout
        """
        self.game_over = False
        self.win = False
        self.player = None
        self.entities = []
        self.board = self.parse_board(board_file)

    def __str__(self):
        """
        The board in string form, can be used for printing the stage
        :return:      board-string
        """

        board_string = ""

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                entities_here = list(filter(lambda entity: entity.x == x and entity.y == y, self.entities))
                if entities_here:
                    board_string += str(entities_here.pop())
                else:
                    board_string += str(self.board[y][x])
            board_string += "\n"

        return board_string

    def update(self):
        for entity in self.entities:
            entity.update()

        if self.player.dead:
            self.game_over = True
            print("You lost. Try again.")

        # Check if any Daleks are left in the entities list, if not - VICTORY
        if not list(filter(lambda board_entity: board_entity.name == "Dalek", self.entities)):
            self.game_over = True
            self.win = True
            print("You won! Congratulations!")

    def get_entity(self, x, y):
        """
        Gets the Entity located at the given x and y coordinates
        :param x:   x-coordinate
        :param y:   y-coordinate
        :return:    returns the Entity gotten, or None if no creature was found.
        """

        for entity in self.entities:
            if entity.x == x and entity.y == y:
                return entity

        return None

    def set_entity(self, entity):
        """
        For creating entities. Since they keep track of their
        own x and y coordinates, we only need to add them to the
        entities list.
        :param entity:     the entity to add
        :return:           (nothing)
        """
        self.entities.append(entity)

    def get_tile(self, x, y):
        """
        Gets the tile at the given x and y coordinates
        :param x:   x-coordinate
        :param y:   y-coordinate
        :return:    Tile object
        """
        return self.board[y][x]

    def get_height(self):
        """
        :return:    height of board
        """
        return len(self.board)

    def get_width(self):
        """ Since all rows must be the same length, we only need to
        check the first row.
        :return:    width of board
        """
        return len(self.board[0])

    def set_tile(self, x, y, tile):
        """
        Sets the tile at the given x and y coordinates to the specified Tile
        :param x:       y-coordinate
        :param y:       x-coordinate
        :type x:        int
        :type y:        int
        :type tile:     Tile
        :param tile:    Tile
        :return:        (nothing)
        """
        if not (isinstance(tile, Tile)):
            raise TypeError("Argument must be a Tile")
        self.board[y][x] = tile

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

        # We make an iterator out of the board-list and go through it
        # to check if all the rows are the same length
        iterator = iter(board)
        # set map_len to the length of the first row
        map_len = len(next(iterator))
        if not all(len(row) == map_len for row in iterator):
            raise ValueError("All rows in map-file must be of equal length!")

        # Replace characters with tiles and put entities into lists
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == ".":
                    board[y][x] = Tile(".")
                elif board[y][x] == "#":
                    board[y][x] = Tile("#")
                elif board[y][x] == "D":
                    dalek = Dalek.Dalek(x, y, self)
                    board[y][x] = Tile(".")
                    self.entities.append(dalek)
                elif board[y][x] == "W":
                    doctor = Doctor.Doctor(x, y, self)
                    board[y][x] = Tile(".")
                    self.entities.append(doctor)
                    self.player = doctor
                else:
                    raise ValueError("The only characters allowed in the map-file are\n . # D W")

        return board
