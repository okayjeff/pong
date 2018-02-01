import pygame

from pong import settings
from pong.models.base import PongObject
from pong.utils import (
    exit_game,
    format_time,
    get_formatted_records,
    save_records_to_file
)


class ModalScreen(PongObject):

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


def show_title_screen(screen, clock):
    title_screen = ModalScreen(
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
                    intro = False

        title_screen.render()
        pygame.display.update()
        clock.tick(15)


def show_game_over_screen(screen, clock, seconds):
    save_records_to_file(seconds)
    game_over_screen = ModalScreen(
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
                    game_over = False

        game_over_screen.render()
        pygame.display.update()
        clock.tick(15)
