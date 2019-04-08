from window import *
from textures import *

class Entity(object):
    def __init(self):
        self.alive = None
        self.x = None
        self.y = None
        self.texture = None

    def draw_self(self, window):
        window.blit(self.texture, (self.x, self.y))

    def move(self, depl):
        if self.left and self.x - depl >= 0: self.x -= depl     
        if self.right and (self.x + self.w) + depl <= self.winW: self.x += depl
        if self.up and self.y - depl >= 0: self.y -= depl
        if self.down and (self.y + self.h) + depl <= self.winH: self.y += depl