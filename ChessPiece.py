import pygame
import pathlib

class ChessPiece:
    SIZE = 50
    def __init__(self, pos: list[int], colour: str, surface):
        self.pos = pos
        self.colour = colour    # this is the pieces color
        self.surface = surface  # game window to draw onto
        self.draw()

    #Moves the piece
    def move(self, final_pos):
        pass

    #Returns a list of avaliable moves
    def avaliable_moves(self):
        pass

    def possible_move(self):
        pass
    
    # Draws the piece at it's position
    def draw(self):
        pass

    #Returns position
    def get_pos(self):
        return self.pos

    #converts position to coordinates on the window 
    def pos_to_cords(self, pos, var:int):
        if var == 0:
            pos[0] = pos[0]*50
            pos[1] = 450-(pos[1]*50)
        else:
            pos[0] = pos[0]//50
            pos[1] = (450-pos[1])//50

        return(pos)


class Pawn(ChessPiece):
    WHITE_IMG = 'sprites/wp.png'
    BLACK_IMG = 'sprites/bp.png'
    
    def move(self, final_pos, white_pieces, black_pieces):
        #This checks if the move is possible
        pos = [0,0]

    def draw(self):

        if self.colour == 'w':
            pawn = pygame.transform.scale(pygame.image.load(self.WHITE_IMG), (self.SIZE, self.SIZE)) 
        else:
            pawn = pygame.transform.scale(pygame.image.load(self.BLACK_IMG), (self.SIZE, self.SIZE)) 

        if self.pos != [0,0]:
            cords = self.pos_to_cords(self.pos, 0) 
            self.surface.blit(pawn, (cords[0], cords[1]))
        
    
    def avaliable_moves(self):
        if (self.colour=='w'):
            pass

    
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

    def en_passant():
        pass
