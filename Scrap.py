import Entity


class Scrap(Entity.Entity):
    """
    A pile of scrap, the result of two Daleks colliding.
    """

    def __init__(self, x, y, world):
        """
        Creates a pile of scrap at the coordinates x, y. Represented by the
        character "%".
        :param x:   x-coordinate
        :param y:   y-coordinate
        """
        self.name = "scrap pile"
        super().__init__(x, y, world, "%")

