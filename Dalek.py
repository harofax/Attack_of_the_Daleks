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

    def collide(self, other, remove_self, remove_other, msg=""):
        """
        Handles a Dalek's collision with other entities.
        :param other:           another Entity object
        :param remove_self:     whether to remove self when checking collision
        :param remove_other:    whether to remove other when checking collision
        :param msg:             flavour text to display on collision
        :return:                (nothing)
        """

        if isinstance(other, Dalek):
            self.world.set_entity(Scrap.Scrap(other.x, other.y, self.world))
            Entity.Entity.collide(self, other, True, True,
                                  "The two Daleks bumped into each other and exploded into a scrap pile")

        if isinstance(other, Scrap.Scrap):
            Entity.Entity.collide(self, other, True, False,
                                  "The Dalek tipped over a scrap pile, INSTANTLY bursting into flames "
                                  "while screaming obscenities at you.")

        if isinstance(other, Doctor.Doctor):
            Entity.Entity.collide(self, other, False, True,
                                  "The Dalek fires its DEATH-BEAM, while shrieking 'EXTERMINATE'. \n"
                                  "You have died")

    def update(self):
        """
        Every turn the Daleks need to go one step towards the Doctor
        :return:    (nothing)
        """
        # You can't hunt what's dead B^)
        # And you can't hunt WHILE dead...
        if not self.dead and not self.world.player.dead:
            self.hunt()

    def hunt(self):
        """
        Method containing pathfinding algorithm used to go towards the Doctor, using
        the move_by method.
        """
        player_x = self.world.player.x
        player_y = self.world.player.y

        def move_x():
            # Calculate the direction in X to move towards player, returns -1 or 1
            if self.x < player_x:
                return 1
            elif self.x > player_x:
                return -1

        def move_y():
            # Calculate the direction in Y to move towards player, returns -1 or 1
            if self.y < player_y:
                return 1
            elif self.y > player_y:
                return -1

        x_dir = 0
        y_dir = 0

        dx = abs(player_x - self.x)
        dy = abs(player_y - self.y)

        # if player is located diagonally from dalek, go towards player
        if dx == dy or (dx == 0 and dy == 0):
            x_dir = move_x()
            y_dir = move_y()

        else:
            # probability of x-movement
            x_move_weight = dx / (dx + dy)
            # probability of y-movement
            y_move_weight = dy / (dx + dy)

            move_probability = random.random()

            if move_probability < x_move_weight:
                x_dir = move_x()
            if move_probability < y_move_weight:
                y_dir = move_y()

        # If walking diagonally and encountering a wall, follow along it
        if self.world.get_tile(self.x + x_dir, self.y + y_dir).is_wall():
            y_wall = self.world.get_tile(self.x, self.y + y_dir).is_wall()
            x_wall = self.world.get_tile(self.x + x_dir, self.y).is_wall()

            #         Y_WALL
            # X_WALL  PLAYER  X_WALL
            #         Y_WALL

            # Check if, when walking diagonally, left/right spaces are free - if so
            # only walk in X-direction, walking along the wall and ignore y-movement
            if not x_wall:
                y_dir = 0
            # See above but for Y-direction
            if not y_wall:
                x_dir = 0

        self.move_by(x_dir, y_dir)
