from window import get_size_window


class Shooter(object):
    life = 100
    x = 0
    y = 0

    def __init__(self, dim):
        self.x = (dim[0] / 2) - 64 / 2
        self.y = dim[1] - 100