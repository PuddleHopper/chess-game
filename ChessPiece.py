import os


class ChessPiece:

    def __init__(self, xpos: int, ypos: int, colour: str):
        self.xpos = xpos    #x position of the piece on the board
        self.ypos = ypos    #y position of the piece on the board
        self.colour = colour    # this is the pieces color

    #Moves the piece
    def Move(self):
        pass

    #Returns a list of avaliable moves
    def AvalMoves(self):
        pass

