import pygame

from pong import settings
from pong.models.base import PongObject


class Ball(PongObject):

    def __init__(self, surf, pos, velocity, color=None):
        self.surf = surf
        self.pos = pos
        self.velocity = velocity
        self.color = color or settings.BALL_COLOR
        super(Ball, self).__init__()

    def get_rect(self):
        left, top = self.pos
        width, height = settings.BALL_THICKNESS, settings.BALL_THICKNESS
        return pygame.Rect(left, top, width, height)

    def render(self):
        pygame.draw.rect(self.surf, self.color, self.rect)
