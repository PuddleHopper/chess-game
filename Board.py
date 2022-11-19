import pygame
import os
import time

#pygame.init()
pygame.font.init()

SIZE = 500
SQUARE_SIZE = SIZE/10
WHITE = (139,69,19)
BLACK = (205,133,63)
MAIN_FONT = pygame.font.SysFont('Segoe UI',20, bold=True)
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
FONT_COLOUR = (255,255,255)

def Setup():
    window = pygame.display.set_mode((SIZE,SIZE))
    pygame.display.set_caption("Chess")
    window.fill((20,20,20))
    DrawBoard(window)
    DrawNum(window)
    pygame.display.update()
    time.sleep(4)


#Draws the checkered board
def DrawBoard(surface):
    x = SIZE/10
    y = SIZE/10

    #row changes between 1 and 0
    row = 1

    #Loops through and draws each of the sqaures draws each
    #row moving down the board
    for i in range(64):
        if x == 450:    #if it's at the end of the row
            y += 50
            x = 50
            if (row == 1):
                row = 0
            else:
                row = 1

        #This is used to create the alternating checkered pattern
        if ((i%2)==row):    
            colour = WHITE
        else:
            colour = BLACK

        pygame.draw.rect(surface,colour, (x,y,SQUARE_SIZE,SQUARE_SIZE)) #draws square
        x += 50     #increments


def DrawNum(surface):
    MAIN_FONT = pygame.font.SysFont('Segoe UI',20, bold=True)
    #This draws the Numbers and Letters on the Board
    start = 60
    for i in range(8):
        text = MAIN_FONT.render(LETTERS[i], True, FONT_COLOUR)
        surface.blit(text, (start,450))
        start+=50

    start = 400
    number = 1
    for i in range(8):
        text = MAIN_FONT.render(str(number), True, FONT_COLOUR)
        surface.blit(text, (30,start))
        start-=50
        number+=1

def DrawPieces(surface):
        #Black Pieces
        b_rook = pygame.transform.scale(pygame.image.load('br.png'), (50, 50))
        b_knight = pygame.transform.scale(pygame.image.load('bk.png'), (50,50))
        b_bishop = pygame.transform.scale(pygame.image.load('bb.png'), (50, 50))
        b_queen = pygame.transform.scale(pygame.image.load('bq.png'), (50, 50))
        b_king = pygame.transform.scale(pygame.image.load('bking.png'), (50, 50)) 
        b_pawn = pygame.transform.scale(pygame.image.load('bp.png'), (50, 50))

        surface.blit(b_rook, (50,50))
        surface.blit(b_rook, (400,50))
        surface.blit(b_knight, (100,50))
        surface.blit(b_knight, (350,50))
        surface.blit(b_bishop, (150,50))
        surface.blit(b_bishop, (300,50)) 
        surface.blit(b_queen, (200,50))
        surface.blit(b_king, (250,50))

        pos = 50
        for i in range(8):
            surface.blit(b_pawn, (pos,100))
            pos += 50

        #White Pieces
        w_rook = pygame.transform.scale(pygame.image.load('wr.png'), (50, 50))
        w_knight = pygame.transform.scale(pygame.image.load('wk.png'), (50,50))
        w_bishop = pygame.transform.scale(pygame.image.load('wb.png'), (50, 50))
        w_queen = pygame.transform.scale(pygame.image.load('wq.png'), (50, 50))
        w_king = pygame.transform.scale(pygame.image.load('wking.png'), (50, 50))
        w_pawn = pygame.transform.scale(pygame.image.load('wp.png'), (50, 50))

        surface.blit(w_rook, (50,400))
        surface.blit(w_rook, (400,400))
        surface.blit(w_knight, (100,400))
        surface.blit(w_knight, (350,400))
        surface.blit(w_bishop, (150,400))
        surface.blit(w_bishop, (300,400)) 
        surface.blit(w_queen, (200,400))
        surface.blit(w_king, (250,400)) 

        pos = 50
        for i in range(8):
            surface.blit(w_pawn, (pos,350))
            pos += 50

Setup()