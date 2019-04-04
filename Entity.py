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
        self.dead = False

    def move_by(self, dx, dy):
        """
        Moves the entity in the specified direction given dx, dy
        :param dx: relative movement in x
        :param dy: relative movement in y
        """
        tile = self.world.get_tile(self.x + dx, self.y + dy)
        creature = self.world.get_entity(self.x + dx, self.y + dy)

        if creature is not None and creature is not self:
            self.collide(creature, False, False)
        if not tile.is_wall():
            self.x += dx
            self.y += dy

    def collide(self, other, remove_self, remove_other, msg=""):
        """
        Handles collision between another entities
        :param other:           another Entity object
        :param remove_self:     whether to remove self when checking collision
        :param remove_other:    whether to remove other when checking collision
        :param msg:             flavour text to display on collision
        :return:                (nothing)
        """
        print(self)
        if msg:
            print(msg)
        if remove_self:
            self.dead = True
            self.world.entities.remove(self)
        if remove_other:
            other.dead = True
            self.world.entities.remove(other)

    def update(self):
        """
        Function that runs every turn, handles updating this entity.
        Meant to be overridden by subclasses that update in specific ways.
        :return:    (nothing)
        """

    def __str__(self):
        """
        Returns the glyph of an Entity
        :return: glyph
        """
        return self.glyph
