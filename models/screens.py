import pygame

from pong import settings
from pong.models.base import PongObject


class ModalScreen(PongObject):

    def __init__(self, surf, title_text, subtitle_text, font=None, color=None):
        self.surf = surf
        self.title_text = title_text
        self.subtitle_text = subtitle_text
        self.font = font or settings.DEFAULT_FONT
        self.color = color or settings.WHITE
        self.title_font = pygame.font.SysFont(
            self.font,
            settings.TITLE_FONT_SIZE,
            bold=True
        )
        self.title_surf = self.title_font.render(
            self.title_text,
            settings.ANTIALIAS,
            self.color
        )
        self.subtitle_font = pygame.font.SysFont(
            self.font,
            settings.SUBTITLE_FONT_SIZE
        )
        self.subtitle_surf = self.subtitle_font.render(
            self.subtitle_text,
            settings.ANTIALIAS,
            self.color
        )
        super(ModalScreen, self).__init__()

    def get_rect(self):
        pass

    def get_title_rect(self):
        rect = self.title_surf.get_rect()
        rect.center = settings.DEAD_CENTER
        return rect

    def get_subtitle_rect(self):
        rect = self.subtitle_surf.get_rect()
        pos = (
            settings.WINDOW_WIDTH // 2,
            settings.WINDOW_HEIGHT - 100
        )
        rect.center = pos
        return rect

    def fill_background(self):
        self.surf.fill(settings.BLACK)

    def render(self):
        self.fill_background()
        self.surf.blit(
            self.title_surf,
            self.get_title_rect()
        )
        self.surf.blit(
            self.subtitle_surf,
            self.get_subtitle_rect()
        )
