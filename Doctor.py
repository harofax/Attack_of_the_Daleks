import Entity
import Dalek
import Scrap
import random


class Doctor(Entity.Entity):
    """
    The Doctor, magnificent time-traveller and destroyer of Daleks
    Attributes:
    screwdriver_cooldown:   the amount of turns/steps left to be able to teleport again
    """

    def __init__(self, x, y, world):
        """
        Creates the Doctor object at the given x, y coordinates with the "W" character
        as the glyph.
        :param x:   the x-coordinate
        :param y:   the y-coordinate
        """
        self.name = "The Doctor"
        self.screwdriver_cooldown = 0
        super().__init__(x, y, world, "W")

    def teleport(self):
        """
        Teleports the doctor to a random non-wall spot on the GameBoard
        """
        target_creature = None
        # (Fancy way of writing while True)
        while "Teleporting" and self.screwdriver_cooldown == 0:
            # Choose a random position
            y = random.randrange(1, self.world.get_height())
            x = random.randrange(1, self.world.get_width())

            # If the position isn't a wall, teleport to it! Otherwise try again.
            if not self.world.get_tile(x, y).is_wall():
                target_creature = self.world.get_entity(x, y)
                self.x = x
                self.y = y
                self.screwdriver_cooldown = 5
                break

        if target_creature is not None and target_creature is not self:
            self.collide(target_creature, True, False, "You materialized inside the " + target_creature.name
                         + " and instantly died.")

    def update(self):
        """
        Every turn the cooldown on the Sonic Screwdriver decreases by 1, until it reaches 0
        :return:
        """
        if self.screwdriver_cooldown != 0:
            self.screwdriver_cooldown -= 1
            print("Teleport cooldown:", self.screwdriver_cooldown)

    def move_by(self, dx, dy):
        scrap = self.world.get_entity(self.x + dx, self.y + dy)

        if isinstance(scrap, Scrap.Scrap):
            print("You BONK into the pile of scrap, slightly burning your eyebrows.")
            return
        else:
            Entity.Entity.move_by(self, dx, dy)

    def collide(self, other, remove_self, remove_other, msg=""):
        """
        Handles the Doctors collision with other entities.
        :param other:           another Entity object
        :param remove_self:     whether to remove self when checking collision
        :param remove_other:    whether to remove other when checking collision
        :param msg:             flavour text to display on collision
        :return:                (nothing)
        """
        if isinstance(other, Dalek.Dalek):
            if not msg:
                msg = "You tackle the Dalek before it disintegrates you with its DEATH-BEAM"
            Entity.Entity.collide(self, other, True, False, msg)


