import pytest
from colorama import Back, Style
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.board import Board, terminal_colors

def test_board_initialization_success():
    columns, rows = 5, 10
    board = Board(columns, rows)
    
    assert board.num_of_columns == columns
    assert board.num_of_rows == rows
    assert board.colors == terminal_colors
    assert len(board.board) == rows
    assert all(len(row) == columns for row in board.board)
    assert all(cell == "  " for row in board.board for cell in row)


@pytest.mark.parametrize("cols, rows, error_msg", [
    (0, 5, "'Board' object can't be initalised with less than 1 column!"),
    (-3, 5, "'Board' object can't be initalised with less than 1 column!"),
    (5, 0, "'Board' object can't be initalised with less than 1 row!"),
    (5, -1, "'Board' object can't be initalised with less than 1 row!"),
])
def test_board_initialization_invalid_dimensions(cols, rows, error_msg):
    with pytest.raises(ValueError) as exc_info:
        Board(cols, rows)
    assert str(exc_info.value) == error_msg


def test_change_row_success():
    board = Board(3, 3)
    new_row = ["RD", "GR", "BL"]
    
    result = board.change_row(1, new_row)
    
    assert result is True
    assert board.board[1] == ["RD", "GR", "BL"]
    
    new_row[0] = "YL"
    assert board.board[1][0] == "RD"


@pytest.mark.parametrize("row_idx, row_data", [
    (3, ["RD", "GR", "BL"]),
    (-1, ["RD", "GR", "BL"]),
    (1, ["RD", "GR"]),
    (1, ["RD", "GR", "BL", "WT"]),
])
def test_change_row_failures(row_idx, row_data):
    board = Board(3, 3)
    original_board = [row[:] for row in board.board]
    
    result = board.change_row(row_idx, row_data)
    
    assert result is False
    assert board.board == original_board


def test_get_formatted_row():
    board = Board(2, 2)
    board.change_row(0, ["RD", "  "])
    
    expected_formatted_row = (
        f"[ {Back.RED}  {Style.RESET_ALL} | "
        f"  {Style.RESET_ALL} ]"
    )
    
    assert board.get_formatted_row(0) == expected_formatted_row


def test_board_string_representation():
    board = Board(2, 2)
    board.change_row(0, ["RD", "GR"])
    board.change_row(1, ["BL", "BK"])
    
    expected_str = (
        f"[ {Back.RED}  {Style.RESET_ALL} | {Back.GREEN}  {Style.RESET_ALL} ]\n"
        f"[ {Back.BLUE}  {Style.RESET_ALL} | {Back.BLACK}  {Style.RESET_ALL} ]"
    )
    
    assert str(board) == expected_str