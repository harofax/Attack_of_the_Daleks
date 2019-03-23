import Entity


class Scrap(Entity):
    """
    A pile of scrap, the result of two Daleks colliding.
    """

    def __init__(self, x, y):
        """
        Creates a pile of scrap at the coordinates x, y. Represented by the
        character "%".
        :param x:   x-coordinate
        :param y:   y-coordinate
        """

    def collide(self, other):
        """
        Handles collision with other Entity objects.
        :param other:   another Entity object
        """

