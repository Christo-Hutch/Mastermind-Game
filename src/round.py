from random import choices

from board import Board

class Round:
    def __init__(self, board: Board):
        self.board: Board = board
        self.responses: list = self.generate_response_list(board.num_of_columns, board.num_of_rows)
        self.first_empty_row: int = 0
        self.remaining_rows: int = board.num_of_rows
        self.code: list = self.generate_random_code()
    
    @staticmethod
    def generate_response_list(column_count: int, row_count: int) -> list:
        return [[' ' for _ in range(column_count)] for _ in range(row_count)]
    
    def generate_random_code(self) -> list:
        available_colors = list(self.board.colors.keys())

        # Remove empty entry from potential colors
        available_colors.remove("  ")
        return choices(available_colors, k = self.board.num_of_columns)
    
    def get_formatted_response_row(self, row_num: int) -> str:
        return f"|" + "|".join(self.responses[row_num]) + "|"
    
    def calculate_response(self, row_guess: list) -> list:
        white_pegs = 0
        black_pegs = 0

        code_remaining = []
        guess_remaining = []

        for c, g in zip(self.code, row_guess):
            if c == g:
                black_pegs += 1
            else:
                code_remaining.append(c)
                guess_remaining.append(g)

        for g in guess_remaining:
            if g in code_remaining:
                white_pegs += 1
                code_remaining.remove(g)

        return (['●'] * black_pegs) + (['○'] * white_pegs) + ([' '] * (self.board.num_of_columns - (black_pegs + white_pegs)))
    
    def get_row_response_formatted(self, row_num: int) -> str:
        return self.board.get_formatted_row(row_num) + "=" + self.get_formatted_response_row(row_num)
    
    def print_round_board(self):
        for r in range(self.board.num_of_rows):
            print(self.get_row_response_formatted(r))

    # Returns True if the attempt was correct
    def attempt_row(self, row_num: int, row_data: list):
        self.board.change_row(row_num, row_data)
        response = self.calculate_response(row_data)
        self.responses[row_num] = response

        if response == (['●'] * self.board.num_of_columns):
            return True
        
        return False