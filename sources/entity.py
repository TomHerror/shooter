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