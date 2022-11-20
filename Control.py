import pygame
import Board
import ChessPiece
import time

class Game:

    def __init__(self):
        pygame.init()
        self.surface = Board.Setup()
        self.white_pieces = self.init_pieces('w')
        self.black_pieces = self.init_pieces('b')
        self.update_board()
        
    #Initalises the pieces 
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

    #Used 
    def update_board(self):
        Board.DrawBoard(self.surface)
        self.draw_pieces()
        pygame.display.update()

    #converts position to coordinates on the window 
    def pos_to_cords(self, old_pos, var:int):
        pos = [1,1]
        if var == 0:
            pos[0] = old_pos[0]*50
            pos[1] = 450-(old_pos[1]*50)
        else:
            pos[0] = old_pos[0]//50
            pos[1] = (500-old_pos[1])//50

        return(pos)


    # Draws the piece at it's position
    def draw(self, piece:ChessPiece.ChessPiece):
        if piece.colour == 'w':
            pawn = pygame.transform.scale(pygame.image.load(piece.WHITE_IMG), (piece.SIZE, piece.SIZE)) 
        else:
            pawn = pygame.transform.scale(pygame.image.load(piece.BLACK_IMG), (piece.SIZE, piece.SIZE)) 

        if piece.pos != [0,0]:
            cords = self.pos_to_cords(piece.get_pos(), 0) 
            self.surface.blit(pawn, (cords[0], cords[1]))

    #Iterates throgh all the pieces and draws them
    def draw_pieces(self):
        for piece in self.white_pieces:
            self.draw(piece)
        
        for piece in self.black_pieces:
            self.draw(piece)

    #Checks if given position is valid
    def valid_pos(self, pos:tuple[int]):
        if (((pos[0] > 0) and (pos[0] < 9)) and ((pos[1] > 0) and (pos[1] < 9))):
            return True
        else:
            return False

    def user_input(self, pos1:tuple[int], pos2:tuple[int], turn:str):
        if (self.valid_pos(pos1) and self.valid_pos(pos2)):
            
            if (turn == 'w'):
                pieces = self.white_pieces
                other_pieces = self.black_pieces
            else:
                pieces = self.black_pieces
                other_pieces = self.white_pieces
            
            #Checks if a piece of that colour exists on position 1 pos1
            if (self.pos_used(pos1, pieces)):
                selected_piece = self.get_pieces(pos1, pieces)

                #Now piece performs own checks to see if move is valid
                if (selected_piece.move(pos2, pieces, other_pieces)):
                    
                    return True

        return False

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces

    #Returns true if the given pos has a chess piece on it
    def pos_used(self, pos:tuple[int], pieces:list[ChessPiece.ChessPiece]):
        pos_list = []
        for piece in pieces:
            if (piece.get_pos() == pos):
                return True
        return False
    
    def get_piece(self, pos:tuple[int], pieces:list[ChessPiece.ChessPiece]):
        for piece in pieces:
            if (piece.get_pos() == pos):
                return pos
        return False
    
    def king_in_check(self, pieces:list[ChessPiece.ChessPiece], other_pieces:list[ChessPiece.ChessPiece]):
        king_pos = [0,0]
        for piece in pieces:
            if (piece.__class__.__name__ == "King"):
                king_pos = piece.get_pos()
                break
        

    def get_possible_moves(self, pieces:list[ChessPiece.ChessPiece]):
        possible_moves = []
        for piece in pieces:
            possible_moves.append(piece.possible_attcks())
        
