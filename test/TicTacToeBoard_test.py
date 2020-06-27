import pytest
from TicTacToeBoard import TicTacToeBoard

def create_tic_tac_toe_board():
    assert TicTacToeBoard().board.shape == (3,3)