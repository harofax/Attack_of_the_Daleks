class Tile:
    """
    A tile on the map, either a floor ".", or a wall "#".
    Attributes:
    glyph:     the character representing the tile
    """
    def __init__(self, glyph):
        """
        Creates a new tile
        :param tile: the character of the tile - either a # or a . depending on tile type
        """
        self.glyph = glyph

    def isWall(self):
        """
        Checks if the tile is a wall tile
        :return: Boolean variable, true if self.tile == "#"
        """

    def __str__(self):
        return self.glyph
