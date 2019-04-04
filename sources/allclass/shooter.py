from window import *
from textures import *
import gameloop


class Shooter(object):
    state = True
    life = None
    x = None
    y = None
    w = None
    h = None
    winW = 0
    winH = 0
    left = False
    right = False
    up = False
    down = False
    texture = None

    def __init__(self, dim, pygame):
        self.w = 64
        self.h = 64
        self.life = 100
        self.winW = dim[0]
        self.winH = dim[1]
        self.x = (dim[0] / 2) - self.w / 2
        self.y = dim[1] - 100
        self.texture = load_shooter(pygame)
        gameloop.entity[0].append(self)
        print(gameloop.entity)

    def move(self):
        depl = 5
        if self.left and self.x - depl >= 0: self.x -= depl     
        if self.right and (self.x + self.w) + depl <= self.winW: self.x += depl
        if self.up and self.y - depl >= 0: self.y -= depl
        if self.down and (self.y + self.h) + depl <= self.winH: self.y += depl

    def shoot(self):
        pass