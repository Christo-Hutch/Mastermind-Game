from colorama import Back, Style, init

init()

terminal_colors = {
    "  ": "",
    "RD": Back.RED,
    "GR": Back.GREEN,
    "YL": Back.YELLOW,
    "BL": Back.BLUE,
    "MG": Back.MAGENTA,
    "CY": Back.CYAN,
    "WT": Back.WHITE,
    "BK": Back.BLACK
}

class Board:
    def __init__(self, column_count: int, row_count: int):        
        if column_count < 1:
            raise ValueError("'Board' object can't be initalised with less than 1 column!")
        
        if row_count < 1:
            raise ValueError("'Board' object can't be initalised with less than 1 row!")
        
        self.num_of_columns: int = column_count
        self.num_of_rows: int = row_count
        self.colors: dict = terminal_colors
        self.board: list = self.generate_board(row_count, column_count)

    @staticmethod
    def generate_board(row_count: int, column_count: int) -> list:
        return [["  " for _ in range(column_count)] for _ in range(row_count)]

    def get_formatted_row(self, row_num: int) -> str:
        colored_row_cells = [f"{self.colors[color]}  {Style.RESET_ALL}" for color in self.board[row_num]]

        return f"[ " + " | ".join(colored_row_cells) + " ]"

    def __str__(self) -> str:
        printable_board_lines: list = []

        for row_num in range(self.num_of_rows):
            printable_board_lines.append(self.get_formatted_row(row_num))

        return "\n".join(printable_board_lines)

    # Returns True for a successful change or False for a failure
    def change_row(self, row_num: int, row: list) -> bool:
        if (0 <= row_num < self.num_of_rows) and (self.num_of_columns == len(row)):
            self.board[row_num] = row[:]
            return True
        
        return False