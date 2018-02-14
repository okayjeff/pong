import pygame

import settings
from models.base import PongObject


class Player(PongObject):

    def __init__(self, name, surf, pos, color=None):
        self.name = name
        self.surf = surf
        self.pos = pos
        self.color = color or settings.PADDLE_COLOR
        super(Player, self).__init__()

    def get_rect(self):
        left, top = self.pos
        width, height = settings.PADDLE_THICKNESS, settings.PADDLE_SIZE
        return pygame.Rect(left, top, width, height)

    def render(self):
        if self.bottom > settings.BOTTOM_EDGE:
            self.bottom = settings.BOTTOM_EDGE

        elif self.top < settings.TOP_EDGE:
            self.top = settings.TOP_EDGE

        return pygame.draw.rect(
            self.surf,
            self.color,
            self.rect
        )

    def hits_ball(self, ball):
        return self.rect.colliderect(ball)