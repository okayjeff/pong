class PongObject(object):

    def __init__(self):
        self.rect = self.get_rect()

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

    @centerx.setter
    def centerx(self, value):
        self.rect.centerx = value

    @property
    def centery(self):
        return self.rect.centery

    @centery.setter
    def centery(self, value):
        self.rect.centery = value

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
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def move(self, vector):
        self.x += vector[0]
        self.y += vector[1]

    def reposition(self, pos):
        self.centerx, self.centery = pos
