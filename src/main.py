from round import Round
from board import Board
from utils import get_colors_tooltip, clean_user_input, clear_terminal

new_board = Board(4, 10)
new_round = Round(new_board)
colors = new_board.colors.copy()
del colors["  "]

while new_round.remaining_rows > 0 and not new_round.isWon:
    clear_terminal()

    print(new_round.code) 
    
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
    print(f"Congratulations! You won! Score: {new_round.get_score()}")
else:
    print(f"Game Over! You ran out of turns. The code was: {' '.join(new_round.code)}")