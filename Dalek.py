import Entity
import Scrap
import Doctor
import random

class Dalek(Entity.Entity):
    """
    A Dalek, murderous robot hunting for the Doctor
    """

    def __init__(self, x, y, world):
        """
        Constructs a new Dalek with the coordinates x, y. Uses the "D" character
        as a glyph
        :param x:   x-coordinate
        :param y:   y-coordinate
        """
        self.name = "Dalek"
        super().__init__(x, y, world, "D")

    def collide(self, other, *msg):
        """
        Handles collision with other entities. In the case of another Dalek,
        both will be destroyed and replaced with a Scrap object. In case of
        the Doctor, the Doctor will be destroyed, triggering the lose-condition.
        :param other:   another Entity object
        :param msg:     message to display on collision
        """
        if isinstance(other, Dalek):
            print("The two daleks bumped into each other and exploded into a pile of scrap")
            self.world.set_entity(Scrap.Scrap(other.x, other.y, self.world))
            self.world.entities.remove(other)
            self.world.entities.remove(self)
            return

        if isinstance(other, Scrap.Scrap):
            print("The dalek STUPIDLY crashed into a pile of scrap, instantly bursting into flames")
            self.world.entities.remove(self)

        if isinstance(other, Doctor.Doctor):
            print("The Dalek fires its BEAM GUN with no mercy, while shrieking 'EXTERMINATE'. \nYou have died.")
            self.world.game_over = True

    def update(self):
        """
        Every turn the Daleks need to go one step towards the Doctor
        :return:    (nothing)
        """
        self.hunt()
        print("EXTERMINATE")

    def hunt(self):
        """
        Method containing the A* algorithm used to go towards the Doctor, using
        the move_by method.
        """
        self.move_by(random.randint(-1, 1), random.randint(-1, 1))


