import pygame

from pong import settings
from pong.models.base import PongObject


class Arena(PongObject):

    def __init__(self, surf, line_color=None, bg_color=None, border_weight=None):
        self.surf = surf
        self.line_color = line_color or settings.ARENA_LINE_COLOR
        self.bg_color = bg_color or settings.ARENA_BGCOLOR
        self.border_weight = border_weight or settings.ARENA_BORDER_THICKNESS
        super(Arena, self).__init__()

    def get_rect(self):
        pass

    def draw_border(self):
        pygame.draw.rect(
            self.surf,
            self.line_color,
            (settings.TOP_LEFT, settings.BOTTOM_RIGHT),
            self.border_weight
        )

    def draw_center_line(self):
        pygame.draw.line(
            self.surf,
            self.line_color,
            settings.MID_TOP,
            settings.MID_BOTTOM,
            settings.LINE_THICKNESS//4
        )

    def fill_background(self):
        self.surf.fill(self.bg_color)

    def render(self):
        self.fill_background()
        self.draw_border()
        self.draw_center_line()
