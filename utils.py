import pygame

from pong import settings


def delay(seconds):
    pygame.time.delay(seconds*1000)


def get_player_default_pos(cpu_player=False):
    if cpu_player:
        x = settings.WINDOW_WIDTH - (settings.PADDLE_THICKNESS + settings.PADDLE_OFFSET)
    else:
        x = settings.PADDLE_OFFSET
    y = (settings.WINDOW_HEIGHT - settings.PADDLE_SIZE) // 2
    return x, y


def get_ball_default_pos():
    x = (settings.WINDOW_WIDTH // 2) - (settings.LINE_THICKNESS // 2)
    y = (settings.WINDOW_HEIGHT // 2) - (settings.LINE_THICKNESS // 2)
    return x, y