from textures import *
from entity import Entity
import entity
from random import randint
import gameloop

class Enemy(Entity):
    def __init__(self, pygame):
        Entity.__init__(self)
        self.alive = 1
        self.x = randint(0, gameloop.dim[0])
        self.y = 10
        self.texture = load_texture(pygame, '../img/enemy/shooter/lvl1.png')
        self.texture = pygame.transform.scale(self.texture, (64, 64))
        gameloop.entity[2].append(self)

    def move(self):
        self.y += 1
        if self.y >= gameloop.dim[1] + 5:
            self.alive = 0


    def draw_self(self, window):
        window.blit(self.texture, (self.x, self.y))