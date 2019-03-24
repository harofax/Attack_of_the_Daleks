from Entity import *


class Dalek(Entity):
    """
    A Dalek, murderous robot hunting for the Doctor
    """

    def __init__(self, x, y):
        """
        Constructs a new Dalek with the coordinates x, y. Uses the "D" character
        as a glyph
        :param x:   x-coordinate
        :param y:   y-coordinate
        """
        super().__init__(x, y, "D")

    def collide(self, other):
        """
        Handles collision with other entities. In the case of another Dalek,
        both will be destroyed and replaced with a Scrap object. In case of
        the Doctor, the Doctor will be destroyed, triggering the lose-condition.
        :param other:   another Entity object
        """

    def hunt(self):
        """
        Method containing the A* algorithm used to go towards the Doctor, using
        the move_by method.
        """


