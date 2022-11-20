import pygame
import time
import Control


def change_turn(turn:str):
    if turn == 'w':
        return 'b'
    else:
        return 'w'

def main():
    Game = Control.Game()

    mouse_pos1 = [0,0] #First selection 
    mouse_pos2 = [0,0] #Second selection
    turn = 'w'  #Indicates which players turn it is

    while (True):
        try:
            for event in pygame.event.get():
                #This stops the program when the X button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pos = Game.pos_to_cords(mouse_pos,1)
                    #print(f"{mouse_pos[0], mouse_pos[1]}")

                    if Game.valid_pos(mouse_pos):
                        if (mouse_pos1 == [0,0]):
                            mouse_pos1 = mouse_pos
                        else:
                            mouse_pos2 = mouse_pos
                            if Game.user_input(mouse_pos1, mouse_pos2, turn):
                                turn = change_turn(turn)
                                
                                
                            mouse_pos1 = [0,0]
                    
            pygame.display.update()
            

        except Exception as e:
            print("Error in App.py main: " + str(e))
            break


if (__name__ == "__main__"):
    main()