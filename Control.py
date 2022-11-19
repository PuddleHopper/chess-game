import pygame
import Board
import ChessPiece

class Game:

    def __init__(self) -> None:
        self.surface = Board.Setup()
        self.white_pieces = self.init_white_pieces()
        self.black_pieces = self.init_black_pieces()
        pygame.display.update()
        

    def init_white_pieces(self):
        piece_list = []

        for i in range(8):
            piece_list.append(ChessPiece.Pawn([i+1,2], 'w', self.surface))

        return piece_list

    def init_black_pieces(self):
        piece_list = []

        for i in range(8):
            piece_list.append(ChessPiece.Pawn([i+1,7], 'b', self.surface))

        return piece_list