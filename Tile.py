class Tile:
    """
    A tile on the map, either a floor ".", or a wall "#".
    Attributes:
    glyph:     the character representing the tile
    """
    def __init__(self, glyph):
        """
        Creates a new tile
        :param glyph: the character of the tile - either a # or a . depending on tile type
        """
        self.glyph = glyph

    def is_wall(self):
        """
        Checks if the tile is a wall tile
        :return: Boolean variable, true if self.tile == "#"
        """
        return self.glyph == "#"

    def __str__(self):
        return self.glyph
