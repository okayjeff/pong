import time

import pygame

from pong import settings
from pong.models.base import PongObject


class Clock(PongObject):
    def __init__(self, surf, pos=None):
        self.surf = surf
        self.pos = pos or settings.MID_TOP
        self.start_time = pygame.time.get_ticks()
        self.color = settings.WHITE
        self.font = self.get_font(settings.DEFAULT_FONT)
        self.font_surf = self.font.render('00:00', settings.ANTIALIAS, self.color, settings.BLACK)
        self.started = False
        super(Clock, self).__init__()

    def get_font(self, font=settings.DEFAULT_FONT, size=settings.CLOCK_FONT_SIZE):
        return pygame.font.SysFont(font, size)

    def get_rect(self):
        return self.font_surf.get_rect()

    def format_time(self, seconds):
        fmt = settings.TIME_FORMAT
        return time.strftime(fmt, time.gmtime(seconds))

    def get_elapsed_seconds(self, now):
        elapsed = (now - self.start_time) // 1000
        return elapsed

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.stop()

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def render(self):
        now = pygame.time.get_ticks()
        text = self.format_time(self.get_elapsed_seconds(now))
        self.font_surf = self.font.render(text, settings.ANTIALIAS, self.color, settings.BLACK)
        self.centerx, self.y = self.pos[0], self.pos[1]+settings.LINE_THICKNESS
        self.surf.blit(self.font_surf, self.rect)