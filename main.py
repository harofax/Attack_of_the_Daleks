from GameBoard import *
import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def setup():
    """
    Sets up the board and initializes the game
    :param board_file:  location of the board file.
    :return:    (nothing)
    """

    print("Welcome!")
    game_board = GameBoard("test-labyrint.txt")
    print(str(game_board))


def update(game_board):
    """
    Waits for user input, then moves Daleks accordingly and checks for the win/lose-condition.
    :return:    nothing
    """
    mov = "q"#input("Command> ").lower()

    if mov == "w": game_board.player.move_by(0, -1)
    elif mov == "x": game_board.player.move_by(0, 1)
    elif mov == "a": game_board.player.move_by(-1, 0)
    elif mov == "d": game_board.player.move_by(1, 0)
    elif mov == "q": game_board.player.move_by(-1, -1)
    elif mov == "e": game_board.player.move_by(1, -1)
    elif mov == "z": game_board.player.move_by(-1, 1)
    elif mov == "c": game_board.player.move_by(1, 1)
    elif mov == "s": game_board.player.move_by(0, 0)
    elif mov == "t": game_board.player.teleport()

    # Maybe just put daleks into separate list in gameboard instead...depends on if scrap is used at all
    for dalek in filter(lambda entity: entity.name == "Dalek", game_board.entities):
        dalek.move_by(random.randint(-1, 1), random.randint(-1, 1))

    print(len(list(filter(lambda entity: entity.name == "Dalek", game_board.entities))))


def draw(game_board):
    """
    Draws the GameBoard and accompanying Entity objects out in the terminal as well
    as the remaining teleport-cooldown
    :return:    nothing
    """
    cls()
    print(str(game_board))


def main():

    print("Welcome!")
    game_board = GameBoard("test-labyrint.txt")
    print(str(game_board))

    while not game_board.game_over:
        update(game_board)
        draw(game_board)


if __name__ == "__main__":
    main()


