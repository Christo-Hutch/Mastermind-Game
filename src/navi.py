from simple_term_menu import TerminalMenu

from game import Game

"""
key: difficulty
value: tuple of (columns, rows)
"""
single_round_difficulties = {"easy": (4, 15),
                             "medium": (4, 10),
                             "hard": (4, 7)}

"""
key: difficulty
value: tuple of (round count, list of round configs)
"""
multi_round_modes = {"short": (2, [{"columns": 4, "rows": 10}, {"columns": 4, "rows": 10}]),
                     "normal": (3, [{"columns": 4, "rows": 10}, {"columns": 4, "rows": 8}, {"columns": 4, "rows": 6}]),
                     "long": (4, [{"columns": 4, "rows": 10}, {"columns": 4, "rows": 10}, {"columns": 4, "rows": 8}, {"columns": 4, "rows": 6}])}

class MenuNavi:
    def __init__(self, user: str):
        self.user = user

    @staticmethod
    def main_menu():
        options = ["Play Game", "Guide", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main Menu")
        menu_entry_index = terminal_menu.show()
        
        match menu_entry_index:
            case 0:
                MenuNavi.select_game_menu()

            case 1:
                pass

            case 2:
                pass

            case _:
                MenuNavi.main_menu()

    @staticmethod
    def select_game_menu():
        options = ["Single Round", "Multiple Rounds", "Go Back"]
        terminal_menu = TerminalMenu(options, title="Play Game")
        menu_entry_index = terminal_menu.show()
        
        match menu_entry_index:
            case 0:
                MenuNavi.single_round_menu()

            case 1:
                pass

            case 2:
                MenuNavi.main_menu()

            case _:
                MenuNavi.select_game_menu()

    @staticmethod
    def single_round_menu():
        options = ["Hard", "Medium", "Easy", "Go Back"]
        terminal_menu = TerminalMenu(options, title="Play Single Round")
        menu_entry_index = terminal_menu.show()
        
        match menu_entry_index:
            case 0:
                new_game = Game(1, [{"columns": single_round_difficulties["hard"][0], "rows": single_round_difficulties["hard"][1]}])

                new_game.play_game()

            case 1:
                new_game = Game(1, [{"columns": single_round_difficulties["medium"][0], "rows": single_round_difficulties["hard"][1]}])

                new_game.play_game()

            case 2:
                new_game = Game(1, [{"columns": single_round_difficulties["easy"][0], "rows": single_round_difficulties["hard"][1]}])

                new_game.play_game()

            case 3:
                MenuNavi.select_game_menu()

            case _:
                MenuNavi.single_round_menu()

        MenuNavi.select_game_menu()

    @staticmethod
    def multi_round_menu():
        options = ["Hard", "Medium", "Easy", "Go Back"]
        terminal_menu = TerminalMenu(options, title="Play Single Round")
        menu_entry_index = terminal_menu.show()
        
        match menu_entry_index:
            case 0:
                new_game = Game(multi_round_modes["hard"][0], multi_round_modes["hard"][1])

                new_game.play_game()

            case 1:
                new_game = Game(multi_round_modes["medium"][0], multi_round_modes["hard"][1])

                new_game.play_game()

            case 2:
                new_game = Game(multi_round_modes["easy"][0], multi_round_modes["hard"][1])

                new_game.play_game()

            case 3:
                MenuNavi.select_game_menu()

            case _:
                MenuNavi.multi_round_menu()