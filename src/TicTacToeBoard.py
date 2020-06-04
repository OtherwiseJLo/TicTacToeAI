import numpy as np

class TicTacToeBoard:
    def __init__(self, n=3):
        self.size = n
        blank_board = [' ']*n*n
        self.board = np.array(blank_board).reshape([n,n])
        
        self.rows = self._get_rows()
        self.columns = self._get_columns()
        self.diagonals = self._get_diagonals()
    
    def _get_rows(self):
        return [''.join(self.board[i, :]) for i in range(self.size)]
        
    def _get_columns(self):
        return [''.join(self.board[:, i]) for i in range(self.size)]
        
    def _get_diagonals(self):
        top_left_bottom_right = self.board.diagonal()
        top_right_bottom_left = np.fliplr(self.board).diagonal()
        return [''.join(diag) for diag in [top_left_bottom_right, top_right_bottom_left]]
        
