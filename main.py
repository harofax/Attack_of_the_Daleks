from GameBoard import *
def setup():
    """
    Sets up the board and initializes the game
    :param board_file:  location of the board file.
    :return:    (nothing)
    """


def update():
    """
    Waits for user input, then moves Daleks accordingly and checks for the win/lose-condition.
    :return:    nothing
    """


def draw():
    """
    Draws the GameBoard and accompanying Entity objects out in the terminal as well
    as the remaining teleport-cooldown
    :return:    nothing
    """


def main():
    print("Welcome!")
    game_board = GameBoard("test-labyrint.txt")



if __name__ == "__main__":
    main()


