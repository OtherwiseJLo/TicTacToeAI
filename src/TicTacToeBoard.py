import numpy as np

class TicTacToeBoard:
    def __init__(self, n=3):
        blank_board = [' ']*n*n
        self.board = np.array(blank_board).reshape([n,n])
        
