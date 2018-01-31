import pygame

from pong import settings
from pong.models.base import PongObject


class Announcement(PongObject):

    def __init__(self, surf, text, font='Courier', color=None, bg_color=None):
        self.surf = surf
        self.text = text
        self.color = color or settings.BLACK
        self.pos = settings.DEAD_CENTER
        self.font_size = settings.ANNOUNCEMENT_FONT_SIZE
        self.font = self.font = pygame.font.SysFont(font, self.font_size)
        self.bg_color = bg_color or settings.WHITE
        super(Announcement, self).__init__()

    def get_rect(self):
        width = settings.ANNOUNCEMENT_WIDTH
        height = settings.ANNOUNCEMENT_HEIGHT
        rect = pygame.Rect(0, 0, width, height)
        rect.center = self.pos
        return rect

    def render(self):
        surf = self.font.render(self.text, False, self.color)
        text_rect = surf.get_rect()
        text_rect.center = self.pos
        pygame.draw.rect(self.surf, self.bg_color, self.rect)
        self.surf.blit(surf, text_rect)
