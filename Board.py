import pygame
import os
import time


## Global Vars
SIZE = 500
SQUARE_SIZE = SIZE/10
WHITE = (139,69,19)
BLACK = (205,133,63)
pygame.font.init()
MAIN_FONT = pygame.font.SysFont('Segoe UI',20, bold=True)
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
FONT_COLOUR = (255,255,255)

def Setup():
    try:
        window = pygame.display.set_mode((SIZE,SIZE))   #Creates window
        pygame.display.set_caption("Chess")  
        window.fill((20,20,20))
        DrawBoard(window)
        DrawNum(window)
        return window

    except Exception as e:
        print("Error in Setup method of Board.py: " + str(e))


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
