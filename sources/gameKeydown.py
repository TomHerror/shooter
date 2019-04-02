import pygame
from pygame.locals import *
from allclass.shooter import *


def game_keydown(pygame, event, shooter, window):

    if event.type == pygame.KEYDOWN:
        if event.key == K_ESCAPE: 
            pygame.quit()
            exit(0)
        elif event.key == K_LEFT: shooter.left = True
        elif event.key == K_RIGHT: shooter.right = True
        elif event.key == K_UP: shooter.up = True
        elif event.key == K_DOWN: shooter.down = True
    elif event.type == pygame.KEYUP:
        if event.key == K_LEFT: shooter.left = False
        elif event.key == K_RIGHT: shooter.right = False
        elif event.key == K_UP: shooter.up = False
        elif event.key == K_DOWN: shooter.down = False
    
