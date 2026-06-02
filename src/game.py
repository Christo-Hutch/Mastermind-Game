from round import Round
from board import Board
from utils import get_colors_tooltip, clean_user_input, clear_terminal

"""
This class is used to start rounds through the use of the methods
within the 'Round' class. When an object is created, it must initalise
with parameters describing the number of rounds and a list of dictionaries
containing the config for each round (dimensions of board, etc.).
"""
class Game:
    def __init__(self, round_count: int, rounds_config: list):
        if round_count < 1:
            raise ValueError("'round_count' can not be less than 1")
        
        if len(rounds_config) != round_count:
            raise ValueError(f"'rounds_config' doesn't contain {round_count} dictionary configs")
        
        """
        Rounds Config is a list of dictionaries, the index of the
        dictionary correlates to the round and the desired config.
        """
        self.rounds_config: list = rounds_config
        self.round_count: int = round_count
        self.total_score: float = 0.0

    def play_round(self, round_num: int, row_count: int, column_count: int):
        new_board = Board(column_count, row_count)
        new_round = Round(new_board)
        colors = new_board.colors.copy()
        del colors["  "]

        while new_round.remaining_rows > 0 and not new_round.isWon:
            clear_terminal()
            
            print(f"---ROUND {round_num}---")
            new_round.print_round_board()
            print(f"You can enter {new_board.num_of_columns} colors:\n" + get_colors_tooltip(colors))

            valid_user_input = False
            clean_input = []
            
            while not valid_user_input:
                user_input = input("Enter your colors: ")
                clean_input = clean_user_input(user_input, colors)

                if len(clean_input) == new_board.num_of_columns:
                    valid_user_input = True

            new_round.attempt_row(clean_input)

        clear_terminal()
        new_round.print_round_board()

        if new_round.isWon:
            round_score = new_round.get_score()
            self.total_score += round_score
            print(f"Congratulations! You won! Score: {round_score}")
        else:
            print(f"Game Over! You ran out of turns. The code was: {' '.join(new_round.code)}")

        print(f"Total Game Score: {self.total_score}")

        input("Press Enter To Continue")

    def play_game(self):
        for round_num in range(1, self.round_count + 1):
            self.play_round(round_num, self.rounds_config[round_num - 1]["rows"], self.rounds_config[round_num - 1]["columns"])

        return self.total_score