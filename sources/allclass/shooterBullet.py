from textures import *
import gameloop

class ShooterBullet(Object):
    state = True
    x = None
    y = None
    texture = None
    damage = 50
    def __init__(self, pygame, x, y):
        self.x = x
        self.y = y
        texture = load_texture(pygame, '../img/enemyBullet.png')
        gameloop.entity[1].append(self)
        print(gameloop.entity)
        pass

    def move(self):
        self.y -= 6
        if self.y < gameloop.dim[1] - 20:
            del self

