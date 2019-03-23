class Entity:
    """
    Generic entity parent class used for Daleks and the Doctor
    Attributes:
    x:      x-coordinate
    y:      y-coordinate
    glyph:  character/symbol representing entity
    world:  the world that the entity inhabits
    """

    def __init__(self, x, y, glyph):
        """
        Creates a new entity
        :param x:       x-coordinate
        :param y:       y-coordinate
        :param glyph:   the character used to represent the entity
        """
        self.x = x
        self.y = y
        self.glyph = glyph

    def move_by(self, dx, dy):
        """
        Moves the entity in the specified direction given dx, dy
        :param dx: relative movement in x
        :param dy: relative movement in y
        """

    def collide(self, other):
        """
        Handles collision between another entity, meant as an abstract method to be overridden
        by subclasses
        :param other:   another Entity object
        :return:        nothing
        """

    def __str__(self):
        """
        Returns the glyph of an Entity
        :return: glyph
        """
