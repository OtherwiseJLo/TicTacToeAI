import numpy as np
from itertools import product
from collections import deque
from random import shuffle

class TicTacToeBoard:
    def __init__(self, n=3):
        self.size = n
        blank_board = [' ']*(n**2)
        self.board = np.array(blank_board).reshape([n,n])
        
        self.rows = self._get_rows()
        self.columns = self._get_columns()
        self.diagonals = self._get_diagonals()

        self.moves = self._calculate_moves()
        shuffle(self.moves)


        self.winning_move = 0
        self.winner = None
    
    def _get_rows(self) -> list:
        return [''.join(self.board[i, :]) for i in range(self.size)]
        
    def _get_columns(self) -> list:
        return [''.join(self.board[:, i]) for i in range(self.size)]
        
    def _get_diagonals(self) -> list:
        top_left_bottom_right = self.board.diagonal()
        top_right_bottom_left = np.fliplr(self.board).diagonal()
        return [''.join(diag) for diag in [top_left_bottom_right, top_right_bottom_left]]
    
    def _calculate_moves(self) -> deque :
        return deque(product(range(self.size), range(self.size)))
        
