import random
import time
from simple_parametric_table import ParametricTable


def main():
    welcome_message = simple_title_frame("TIC TAC TOE")
    print(welcome_message)
    print("Choose game mode:\n")
    game_mode = input("(1) Player vs. Player\n(2) Player vs. CPU (very easy)\n")
    if game_mode == "1":
        player_vs_player()
    elif game_mode == "2":
        player_vs_cpu()
    else:
        print("Please choose correct game mode!")
        time.sleep(3)
        main()


def player_vs_player():
    # choose starting player randomly
    starting_player = random.randint(a=1, b=2)
    # show users which players start the game
    # one of the players is an "odd number player", other "even number player"
    # used to distinguish what sign will be placed
    if starting_player == 1:
        print(30 * "-" + "\n' X ' starts the game")
        turn = 1
    else:
        print(30 * "-" + "\n' O ' stars the game")
        turn = 2
    # prepare empty game board out of parametric table
    game_board = ParametricTable(title="TIC TAC TOE", rows=3, columns=3)
    game_board.create_title()
    game_board.table_content()
    game_board.update_table_data()
    # show users what are the names of the fields to choose where to place their sign
    field_names = simple_title_frame("FIELD NAMES")
    print(field_names)
    example_board = fields_table
    example_board()
    # take user input where player puts the sign
    player_input(game_board, turn)


def player_vs_cpu():
    # choose starting player randomly
    starting_player = random.randint(a=1, b=2)
    # show user if player or CPU start the game
    # one of the players is an "odd number player", other "even number player"
    # used to distinguish what sign will be placed
    if starting_player == 1:
        print(30 * "-" + "\nPlayer ' X ' starts the game")
        turn = 1
    else:
        print(30 * "-" + "\nCPU ' O ' stars the game")
        turn = 2
    # prepare empty game board out of parametric table
    game_board = ParametricTable(title="TIC TAC TOE", rows=3, columns=3)
    game_board.create_title()
    game_board.table_content()
    game_board.update_table_data()
    # show users what are the names of the fields to choose where to place their sign
    field_names = simple_title_frame("FIELD NAMES")
    print(field_names)
    example_board = fields_table
    example_board()
    # if user starts, run user input function
    if turn == 1:
        player_input(game_board, turn, cpu=True)
    else:
        cpu_turn(game_board)


def cpu_turn(game_board):
    # dumb CPU opponent
    # create list of possible fields to fill
    possible_fields = list()
    for field in game_board.content.keys():
        if game_board.content[field] == "":
            possible_fields.append(field)
    # choose random field from all possibilities
    cpu_field = random.randint(0, (len(possible_fields) - 1))
    # set CPU sign in that field
    game_board.content[possible_fields[cpu_field]] = "O"
    # update game board
    game_board.update_table_data()
    # check if CPU has won
    if check_if_won(game_board):
        player_input(game_board, turn=2, cpu=True, sign="X")


def player_input(game_board, turn, sign="", cpu=False):
    # show users current board state
    game_board.print_table()
    if sign == "":
        # if "even player" was drawn set player sign to "X"
        if turn % 2:
            sign = "X"
        else:
            sign = "O"
    # take user input and sanitize it
    choose_field = input("Please choose a field to place a sign: (e.g. 'B2', fields table above.)\n").upper().strip()
    # check if chosen field is part of board game
    if choose_field in game_board.content.keys():
        # check if chosen field is an empty one, if yes, place user sign there
        if game_board.content[choose_field] == "":
            game_board.content[choose_field] = sign
            # update board view
            game_board.update_table_data()
        else:
            print("\nFIELD ALREADY TAKEN!")
            player_input(game_board, turn)
    else:
        print("\nPlease write correct field name!")
    # increase turn value to switch to another player
    if cpu is False:
        turn += 1
        # check if any player has won, if not repeat taking user input until one of the players win
        while check_if_won(game_board):
            player_input(game_board, turn)
    else:
        if check_if_won(game_board):
            cpu_turn(game_board)


def check_if_won(game_board):
    # possible winning scenarios
    winning_fields = [
        ["A0", "B0", "C0"],
        ["A1", "B1", "C1"],
        ["A2", "B2", "C2"],
        ["A0", "A1", "A2"],
        ["B0", "B1", "B2"],
        ["C0", "C1", "C2"],
        ["A0", "B1", "C2"],
        ["C0", "B1", "A2"],
    ]
    # check if any of previous winning field arrangements are met
    for arrangement in winning_fields:
        counter_x = 0
        counter_o = 0
        # if field contains player sign, count that field in,
        for field in arrangement:
            if game_board.content[field] == "X":
                counter_x += 1
            elif game_board.content[field] == "O":
                counter_o += 1
            # when three fields are filled from above scenarios player wins
            if counter_o == 3:
                game_board.print_table()
                print("GAME OVER\n' O ' WINS!'")
                quit()
            elif counter_x == 3:
                game_board.print_table()
                print("GAME OVER\n' X ' WINS!")
                quit()
    # when players do not fill three fields from scenarios and all fields are filled with signs, quit the game
    if "" not in game_board.content.values():
        game_board.print_table()
        print("GAME OVER\n Nobody wins.")
        quit()
    return True


def fields_table():
    # prepare example game board to show users what are the fields names
    game_fields = ParametricTable(rows=3, columns=3, cell_width=6)
    game_fields.table_content()
    for key in game_fields.content.keys():
        game_fields.content[key] = key
    game_fields.update_table_data()
    game_fields.print_table()


def simple_title_frame(text):
    """Creates simple frame around statement."""
    text_length = len(text)
    frame_symbol = "#"
    top_bar = ((2 * text_length) * frame_symbol) + "\n"
    middle_bar = frame_symbol + ((int(text_length / 2) - 1) * " ") + text + \
                 ((int(text_length / 2) - 1) * " ") + frame_symbol + "\n"
    bottom_bar = ((2 * text_length) * frame_symbol)
    frame = top_bar + middle_bar + bottom_bar
    return frame


if __name__ == "__main__":
    main()
