import numpy as np

class TicTacToeBoard:
    def __init__(self, n=3):
        blank_board = [' ']*n*n
        self.board = np.array(blank_board).reshape([n,n])
        
        self.rows = self._get_rows()
        self.columns = self._get_columns()
        self.diagonals = self._get_diagonals()
    
    def _get_rows(self):
        pass
        
    def _get_columns(self):
        pass
        
    def _get_diagonals(self):
        pass
        
