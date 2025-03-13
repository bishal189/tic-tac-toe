import pytest
from tic_tac_toe.game import TicTacToe

def test_make_move():
    game = TicTacToe()
    assert game.make_move(0, "X") == True
    assert game.board[0] == "X"

def test_winner():
    game = TicTacToe()
    game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert game.check_winner("X") == True
