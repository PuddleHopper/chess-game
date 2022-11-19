import pygame
import time
import Control

Game = Control.Game()
i = 0
while (i < 5):
    try:
        
        i += 1
        time.sleep(4)
        pygame.display.update()
        

    except Exception as e:
        print("Error in App.py main: " + str(e))
        break