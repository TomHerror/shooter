from textures import *
import gameloop
from entity import Entity
import entity

class ShooterBullet(Entity):
    """"
    state = True
    x = None
    y = None
    texture = None
    """
    damage = 50
    def __init__(self, pygame, x, y):
        Entity.__init__(self)
        self.alive = 1
        self.x = x + 16
        self.y = y
        self.texture = load_texture(pygame, '../img/enemyBullet.png')
        gameloop.entity[1].append(self)
        pass

    def move(self):
        self.y -= 10
        if self.y < - 20:
            self.alive = 0
            

    def __del__(self):
        del self
        pass

