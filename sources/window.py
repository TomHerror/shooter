import pygame
from pygame.locals import *

def init_window():
    """
    initialise la window pygame
    """
    size = (550, 750)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("My First Game")

    return window

def get_size_window():
    """
    return dim avec x et y qui 
    seront egales aux dimensions de la fenetre
    """
    x, y = pygame.display.get_surface().get_size()
    dim = [x, y]
    return dim
