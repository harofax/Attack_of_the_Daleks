from Entity import *


class Doctor(Entity):
    """
    The Doctor, magnificent time-traveller and destroyer of Daleks
    Attributes:
    screwdriver_cooldown:   the amount of turns/steps left to be able to teleport again
    """

    def __init__(self, x, y):
        """
        Creates the Doctor object at the given x, y coordinates with the "W" character
        as the glyph.
        :param x:   the x-coordinate
        :param y:   the y-coordinate
        """
        super().__init__(x, y, "W")

    def teleport(self):
        """
        Teleports the doctor to a random non-wall spot on the GameBoard
        """

    def collide(self, other):
        """
        Handles collision with other entities, such as Daleks and Scrap piles.
        :param other:   another Entity object
        """

