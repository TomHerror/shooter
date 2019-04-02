import os, sys
import pygame
from pygame.locals import *
from window import *
from gameloop import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

pygame.init()

window = init_window()
gameLoop(window, pygame)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
