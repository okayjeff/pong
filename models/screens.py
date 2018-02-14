import pygame

import settings
from models.base import PongObject
from models.sounds import SoundController
from utils.helpers import exit_game, format_time
from utils.records import get_formatted_records, save_records_to_file


class GameIntroScreen(PongObject):

    def __init__(self, surf, title_text, subtitle_text, records=None, font=None, color=None):
        self.surf = surf
        self.title_text = title_text
        self.subtitle_text = subtitle_text
        self.records = records
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
        super(GameIntroScreen, self).__init__()

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

    def fill_background(self, color):
        self.surf.fill(color)

    def render_title(self):
        return self.surf.blit(self.title_surf, self.get_title_rect())

    def render_subtitle(self):
        return self.surf.blit(self.subtitle_surf, self.get_subtitle_rect())

    def render(self):
        self.fill_background(settings.BLACK)
        self.render_title()
        self.render_subtitle()


# TODO: Inheriting from GameIntroScreen is messy
class GameOverScreen(GameIntroScreen):

    def get_title_rect(self):
        rect = self.title_surf.get_rect()
        rect.center = settings.DEAD_CENTER
        rect.centerx = settings.DEAD_CENTER[0]
        rect.centery = settings.DEAD_CENTER[1] - (settings.WINDOW_HEIGHT//4)
        return rect

    def render(self):
        super(GameOverScreen, self).render()
        records_surf = self.get_record_surf()
        records_surf_rect = records_surf.get_rect()
        records_surf_rect.centerx = settings.DEAD_CENTER[0]
        records_surf_rect.centery = settings.DEAD_CENTER[1] + 50
        self.surf.blit(records_surf, records_surf_rect)

    def get_record_surf(self):
        surf = pygame.Surface((300, 200))
        surf.fill(settings.BLACK)
        font = pygame.font.SysFont(
            self.font,
            settings.DEFAULT_FONT_SIZE+6,
            bold=True
        )
        font_surf = font.render(
            'High Scores',
            settings.ANTIALIAS,
            settings.WHITE
        )
        font_rect = font_surf.get_rect()
        font_rect.centerx = surf.get_width()//2
        surf.blit(font_surf, font_rect)

        offset = 40
        for record in self.records:
            f = pygame.font.SysFont(
                self.font,
                settings.DEFAULT_FONT_SIZE+4,
            )
            f_surf = f.render(str(record), settings.ANTIALIAS, settings.WHITE)
            f_rect = f_surf.get_rect()
            f_rect.centerx = surf.get_width()//2
            f_rect.centery = offset
            surf.blit(f_surf, f_rect)
            offset += 25

        return surf


def show_title_screen(screen, clock):
    title_screen = GameIntroScreen(
        surf=screen,
        title_text=settings.GAME_NAME,
        subtitle_text='Press the SPACE bar to start playing.'
    )

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SoundController.play_new_game()
                    intro = False

        title_screen.render()
        pygame.display.update()
        clock.tick(15)


def show_game_over_screen(screen, clock, seconds):
    save_records_to_file(seconds)
    game_over_screen = GameOverScreen(
        surf=screen,
        title_text=format_time(seconds),
        subtitle_text='Press the SPACE bar to play again.',
        records=get_formatted_records()
    )

    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SoundController.play_new_game()
                    game_over = False

        game_over_screen.render()
        pygame.display.update()
        clock.tick(15)
