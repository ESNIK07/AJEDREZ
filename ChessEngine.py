"""
This class is responsible for storing all the information about the current state state of a chess game.
It will also be responsible for determining the valid moves at the current state.
It will also keep a move log.
"""

class GameState():
    def __init__(self):
        #board is an 8x8 2d list, each elemnt of the list has 2 characters.
        #the first caracter represents the color of the piece, 'b' or 'w'
        #the secord caracter represents the type of the piece, 'K', 'Q', 'R', 'B', 'K', 'p' 
        #"--" represents an empty space with no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bR", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "bK", "wR", "wN", "wR"]
        ]
        self.white_to_move = True
        self.movelog = []
        
        