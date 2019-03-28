from GameBoard import *
import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def update(game_board):
    """
    Waits for user input, then moves Daleks accordingly and checks for the win/lose-condition.
    :return:    nothing
    """
    mov = input("Command> ").lower()

    if mov == "w":
        game_board.player.move_by(0, -1)
    elif mov == "x":
        game_board.player.move_by(0, 1)
    elif mov == "a":
        game_board.player.move_by(-1, 0)
    elif mov == "d":
        game_board.player.move_by(1, 0)
    elif mov == "q":
        game_board.player.move_by(-1, -1)
    elif mov == "e":
        game_board.player.move_by(1, -1)
    elif mov == "z":
        game_board.player.move_by(-1, 1)
    elif mov == "c":
        game_board.player.move_by(1, 1)
    elif mov == "s":
        game_board.player.move_by(0, 0)
    elif mov == "t":
        game_board.player.teleport()

    # Maybe just put daleks into separate list in gameboard instead...depends on if scrap is used at all

    print(len(list(filter(lambda entity: entity.name == "Dalek", game_board.entities))))
    game_board.update()


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
    while "Asking for map file":
        board_file = input("Please enter the name of the board you want to load: ")
        try:
            game_board = GameBoard(board_file)
            break
        except ValueError as ve:
            print(str(ve))
        except FileNotFoundError as fnf:
            print("The file %s does not exist!" % fnf.filename)

    print(str(game_board))

    while not game_board.game_over:
        update(game_board)
        draw(game_board)


if __name__ == "__main__":
    main()
