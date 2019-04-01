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
        while "Teleporting" and self.screwdriver_cooldown == 0:
            # Choose a random position
            y = random.randrange(1, self.world.get_height())
            x = random.randrange(1, self.world.get_width(y))

            # If the position isn't a wall, teleport to it! Otherwise try again.
            if not self.world.get_tile(x, y).is_wall():
                target_creature = self.world.get_entity(x, y)
                self.x = x
                self.y = y
                self.screwdriver_cooldown = 5
                break

        if target_creature is not None and target_creature is not self:
            self.collide(target_creature, "You materialized inside the " + target_creature.name
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
            return
        else:
            Entity.Entity.move_by(self, dx, dy)

    def collide(self, other, *msg):
        """
        Handles collision with other entities, such as Daleks and Scrap piles.
        :param other:   another Entity object
        :param msg:     message to display on collision
        """

        if isinstance(other, Dalek.Dalek):
            if msg:
                print(msg)
            else:
                print("You tackle the Dalek before it disintegrates you with its beam of DEATH.")
            self.world.entities.remove(self)


