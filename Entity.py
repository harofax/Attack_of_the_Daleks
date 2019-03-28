class Entity:
    """
    Generic entity parent class used for Daleks and the Doctor
    Attributes:
    x:      x-coordinate
    y:      y-coordinate
    glyph:  character/symbol representing entity
    world:  the world that the entity inhabits
    """

    def __init__(self, x, y, world, glyph):
        """
        Creates a new entity
        :param x:       x-coordinate
        :param y:       y-coordinate
        :param glyph:   the character used to represent the entity
        """
        self.x = x
        self.y = y
        self.world = world
        self.glyph = glyph

    def move_by(self, dx, dy):
        """
        Moves the entity in the specified direction given dx, dy
        :param dx: relative movement in x
        :param dy: relative movement in y
        """
        tile = self.world.get_tile(self.x+dx, self.y+dy)
        creature = self.world.get_entity(self.x+dx, self.y+dy)

        if creature is not None and creature is not self:
            self.collide(creature)
        if not tile.isWall():
            self.x += dx
            self.y += dy

    def collide(self, other, *msg):
        """
        Handles collision between another entity, meant as an abstract method to be overridden
        by subclasses
        :param other:   another Entity object
        :return:        nothing
        """


    def update(self):
        """
        Function that runs every turn, handles updating this entity.
        :return:    (nothing)
        """

    def __str__(self):
        """
        Returns the glyph of an Entity
        :return: glyph
        """
        return self.glyph
