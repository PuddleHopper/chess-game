import pygame
import pathlib

class ChessPiece:
    SIZE = 50
    WHITE_IMG = 'sprites/wp.png'
    BLACK_IMG = 'sprites/bp.png'

    def __init__(self, pos: list[int], colour: str, surface, first_move=True):
        self.pos = pos
        self.colour = colour    # this is the pieces color
        self.surface = surface  # game window to draw onto
        self.first_move = first_move

    #Moves the piece
    def move(self, final_pos):
        pass

    #Returns a list of avaliable moves
    def avaliable_moves(self):
        pass

    def possible_attacks(self):
        pass

    #Returns position
    def get_pos(self):
        return self.pos

    def set_pos(self, pos:tuple[int]):
        self.pos = pos


class Pawn(ChessPiece):
    WHITE_IMG = 'sprites/wp.png'
    BLACK_IMG = 'sprites/bp.png'
    
    def move(self, final_pos, white_pieces, black_pieces):
        #This checks if the move is possible
        self.first_move = False
        
    
    def avaliable_moves(self):
        moves = self.possible_moves

    def possible_moves(self):
        moves = []

        if self.colour == 'w':
            moves.append(self.pos[0], self.pos[1]+1)   #Pawn moves forward
            moves.append(self.pos[0]+1, self.pos[1]+1)   #Pawn takes to the left
            moves.append(self.pos[0]-1, self.pos[1]+1)   #Pawn take to the right

        elif self.colour == 'b':
            moves.append(self.pos[0], self.pos[1]-1)   #Pawn moves forward
            moves.append(self.pos[0]+1, self.pos[1]-1)   #Pawn takes to the left
            moves.append(self.pos[0]-1, self.pos[1]-1)   #Pawn take to the right
        else:
            print("Invalid colour assigned to Pawn")

        return moves
        
    #Returns list of positions of attack
    def possible_attacks(self):
        attacks = []
        if (self.colour == 'w'):
            attacks.append([self.pos[0]+1, self.pos[1]+1])
            attacks.append([self.pos[0]-1, self.pos[1]+1])
        else:
            attacks.append([self.pos[0]+1, self.pos[1]-1])
            attacks.append([self.pos[0]-1, self.pos[1]-1])

        return attacks

    def standard_move(self):
        pass

    def en_passant(self, black_pieces):
        pass


class Knight(ChessPiece):
    WHITE_IMG = 'sprites/wk.png'
    BLACK_IMG = 'sprites/bk.png'

    def move(self, final_pos: list[int], white_pieces, blacl_pieces):
        pass

    def avaliable_moves(self):
        return super().avaliable_moves()


class Rook(ChessPiece):
    WHITE_IMG = 'sprites/wr.png'
    BLACK_IMG = 'sprites/br.png'

    def move(self, final_pos: list[int], white_pieces, blacl_pieces):
        pass

    def avaliable_moves(self):
        return super().avaliable_moves()


class Bishop(ChessPiece):
    WHITE_IMG = 'sprites/wb.png'
    BLACK_IMG = 'sprites/bb.png'

    def move(self, final_pos: list[int], white_pieces, blacl_pieces):
        pass

    def avaliable_moves(self):
        return super().avaliable_moves()


class Queen(ChessPiece):
    WHITE_IMG = 'sprites/wq.png'
    BLACK_IMG = 'sprites/bq.png'

    def move(self, final_pos: list[int], white_pieces, blacl_pieces):
        pass

    def avaliable_moves(self):
        return super().avaliable_moves()


class King(ChessPiece):
    WHITE_IMG = 'sprites/wking.png'
    BLACK_IMG = 'sprites/bking.png'

    def move(self, final_pos: list[int], white_pieces, blacl_pieces):
        pass

    def avaliable_moves(self):
        return super().avaliable_moves()


def get_all_pieces():
    return ChessPiece.all