import pygame

import settings
from models.base import PongObject


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

    def hits_top_edge(self):
        return self.top <= settings.TOP_EDGE

    def hits_bottom_edge(self):
        return self.bottom >= settings.BOTTOM_EDGE

    def reset_velocity(self):
        self.velocity = [settings.DEFAULT_SPEED, settings.DEFAULT_SPEED]

    def is_moving_left(self):
        return self.velocity[0] < 0

    def is_moving_right(self):
        return self.velocity[0] > 0