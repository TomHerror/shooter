from window import *
from textures import *
import gameloop
from entity import Entity
import entity
from .shooterBullet import *

class Shooter(Entity):

    def __init__(self, dim, pygame):
        Entity.__init__(self)
        self.alive = 1
        self.w = 64
        self.h = 64
        self.life = 100
        self.winW = dim[0]
        self.winH = dim[1]
        self.x = (dim[0] / 2) - self.w / 2
        self.y = dim[1] - 100
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.isShooting = False
        self.texture = load_shooter(pygame)
        self.delay = [20, 20]
        gameloop.entity[0].append(self)
        print(self.alive)

    def shoot(self, pygame):
        if self.delay[1] == self.delay[0]:
            bullet = ShooterBullet(pygame, self.x, self.y)
            self.delay[1] = 0
        else:
            self.delay[1] += 1

    def move(self, depl):
        if self.left and self.x - depl >= 0: self.x -= depl     
        if self.right and (self.x + self.w) + depl <= self.winW: self.x += depl
        if self.up and self.y - depl >= 0: self.y -= depl
        if self.down and (self.y + self.h) + depl <= self.winH: self.y += depl