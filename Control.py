import pygame
import Board
import ChessPiece

class Game:

    def __init__(self) -> None:
        self.surface = Board.Setup()
        self.white_pieces = self.init_pieces('w')
        self.black_pieces = self.init_pieces('b')
        pygame.display.update()
        
    #Initakises the pieces 
    def init_pieces(self, piece_colour):
        piece_list = []

        if piece_colour == 'w':
            #how much the y position of the pieces needs to change base upon colour
            y_change = 0   
            pawn_change = 0
        else:
            y_change = 7
            pawn_change = 5

        #Create Pawns
        for i in range(8):
            piece_list.append(ChessPiece.Pawn([i+1,2+pawn_change], piece_colour, self.surface))

        #Create Knights
        piece_list.append(ChessPiece.Knight([2,1+y_change], piece_colour, self.surface))
        piece_list.append(ChessPiece.Knight([7,1+y_change], piece_colour, self.surface))

        #Create Bishops
        piece_list.append(ChessPiece.Bishop([3,1+y_change], piece_colour, self.surface))
        piece_list.append(ChessPiece.Bishop([6,1+y_change], piece_colour, self.surface))

        #Create Rooks
        piece_list.append(ChessPiece.Rook([1,1+y_change], piece_colour, self.surface))
        piece_list.append(ChessPiece.Rook([8,1+y_change], piece_colour, self.surface))

        #Create Queen
        piece_list.append(ChessPiece.Queen([4,1+y_change], piece_colour, self.surface))

        #Create Kind
        piece_list.append(ChessPiece.King([5,1+y_change], piece_colour, self.surface))

        return piece_list
