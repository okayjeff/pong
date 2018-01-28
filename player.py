import pygame


class Player(object):

    def __init__(self, name, surf, conf, cpu=False):
        self.name = name
        self.surf = surf
        self.conf = conf
        self.pos = self.get_default_pos(cpu)
        self.rect = self.get_rect()

    def get_default_pos(self, cpu):
        if cpu:
            x = self.conf.WINDOW_WIDTH - (self.conf.PADDLE_THICKNESS + self.conf.PADDLE_OFFSET)
        else:
            x = self.conf.PADDLE_OFFSET
        y = (self.conf.WINDOW_HEIGHT - self.conf.PADDLE_SIZE) // 2
        return x, y

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value

    @property
    def centerx(self):
        return self.rect.centerx

    @property
    def centery(self):
        return self.rect.centery

    @property
    def top(self):
        return self.rect.top

    @top.setter
    def top(self, value):
        self.rect.top = value

    @property
    def bottom(self):
        return self.rect.bottom

    @bottom.setter
    def bottom(self, value):
        self.rect.bottom = value

    @property
    def left(self):
        return self.rect.left

    @left.setter
    def left(self, value):
        self.rect.left = value

    @property
    def right(self):
        return self.rect.right

    @right.setter
    def right(self, value):
        self.rect.right = value

    def get_rect(self):
        left, top = self.pos
        width, height = self.conf.PADDLE_THICKNESS, self.conf.PADDLE_SIZE
        return pygame.Rect(left, top, width, height)

    def render(self):
        if self.bottom > self.conf.BOTTOM_EDGE:
            self.bottom = self.conf.BOTTOM_EDGE

        elif self.top < self.conf.TOP_EDGE:
            self.top = self.conf.TOP_EDGE

        return pygame.draw.rect(
            self.surf,
            self.conf.PADDLE_COLOR,
            self.rect
        )

    def move(self, pos):
        self.x += pos[0]
        self.y += pos[1]
