import pygame

from pong import settings
from pong.models.base import PongObject


class Scoreboard(PongObject):

    def __init__(self, surf, scores, font='Courier', size=None, color=None):
        self.surf = surf
        self.pos = self.get_default_pos()
        self.scores = scores
        self.size = size or settings.SCOREBOARD_FONT_SIZE
        self.font = pygame.font.SysFont(font, self.size, bold=True)
        self.color = color or settings.SCOREBOARD_FONT_COLOR
        self.p1_score, self.p2_score = self.get_player_scores()
        self.score_surf = self.font.render(
            '{} {}'.format(self.p1_score, self.p2_score),
            False, self.color
        )
        super(Scoreboard, self).__init__()

    def get_default_pos(self):
        return settings.MID_TOP

    def get_rect(self):
        return self.score_surf.get_rect()

    def get_player_scores(self):
        p1_scores = self.scores[settings.PLAYER_ONE]
        p2_scores = self.scores[settings.PLAYER_TWO]
        return p1_scores, p2_scores

    def render(self):
        p1_score, p2_score = self.get_player_scores()
        self.score_surf = self.font.render(
            '{} {}'.format(p1_score, p2_score),
            settings.ANTIALIAS, self.color
        )
        self.centerx, self.y = self.pos
        self.surf.blit(self.score_surf, self.rect)
