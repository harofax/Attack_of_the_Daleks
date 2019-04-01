from GameBoard import *
import os


def cls():
    """
    A function for clearing the terminal window so that the printing
    of the screen "replaces" the previous print instead of printing
    below it.

    Works for Windows, MacOS and Linux.

    cls = clear command in Windows CMD
    clear = clear command in Linux and Windows Powershell, MacOS
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def setup():
    print("*************************")
    print("*   WELCOME          D  *")
    print("*  TO THE DALEK  =>-/.\\ *")
    print("*     INVASION     /___\\*")
    print("*************************")

    print("Type ANYTHING to play the game")
    print("( or HELP to get instructions )")

    if input("> ").upper() == "HELP":
        print(" REVOLUTIONARY 8-DIRECTIONAL MOVEMENT:")
        print(" [q]   [w]   [e]")
        print("     \\  |  /         PRESS [T]")
        print(" [a] - [s] - [d]    TO TELEPORT")
        print("     /  |  \\")
        print(" [z]   [x]   [c]")
        input("> [ENTER] ")
        cls()
        print(" * AVOID THE DALEKS UNTIL THEY ARE ALL DEAD")
        print(" * IF THEY BUMP INTO EACH OTHER, THEY DIE.")
        print(" * HORRIBLY.")
        print(" * THEY ALSO DIE WHEN THEY CRASH INTO A PILE")
        print(" * OF DEAD DALEKS, SOMETHING TO DO WITH")
        print(" * QUANTUM ENERGIES OR LOOSE DEATH-BEAM-FUEL.")
        print(" * WHO KNOWS.")
        print("          >DON'T DIE< ")
        input("> [ENTER] ")


def update(game_board, player_input):
    """
    Waits for user input, then moves Daleks accordingly and checks for the win/lose-condition.
    :return:    nothing
    """

    if player_input == "w":
        game_board.player.move_by(0, -1)
    elif player_input == "x":
        game_board.player.move_by(0, 1)
    elif player_input == "a":
        game_board.player.move_by(-1, 0)
    elif player_input == "d":
        game_board.player.move_by(1, 0)
    elif player_input == "q":
        game_board.player.move_by(-1, -1)
    elif player_input == "e":
        game_board.player.move_by(1, -1)
    elif player_input == "z":
        game_board.player.move_by(-1, 1)
    elif player_input == "c":
        game_board.player.move_by(1, 1)
    elif player_input == "s":
        game_board.player.move_by(0, 0)
    elif player_input == "t":
        game_board.player.teleport()

    print("EVENTS: ")
    game_board.update()


def draw(game_board):
    """
    Draws the GameBoard and accompanying Entity objects out in the terminal as well
    as the remaining teleport-cooldown
    :return:    nothing
    """

    print(str(game_board))


valid_commands = "qweasdzxct"


def get_player_input():
    """
    Asks player for input until valid input is given
    :return:    a valid player command
    """
    while "No valid input given":
        print("Enter your command: ")
        player_command = input("> ").lower()
        if player_command in valid_commands and len(player_command) == 1:
            return player_command
        else:
            print("Please enter a valid command.")


def main():
    setup()
    cls()
    print("Welcome!")
    restart = True
    while restart:
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
            player_input = get_player_input()
            cls()
            update(game_board, player_input)
            draw(game_board)

        while "Asking for re-match":
            cls()
            print("**********************")
            print("*   ________    [END]*")
            print("*  /[][][][]\\        *")
            print("*  \\________/=<<<    *")
            print("**********************")
            again = input("Play again? (Y/N) ").upper()
            if again == "N":
                restart = False
                print("Goodbye!")
                break
            if again == "Y":
                break
            else:
                print("Please type either Y or N.")


if __name__ == "__main__":
    main()
