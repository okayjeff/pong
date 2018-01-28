import pygame

from pong import settings


def delay(seconds):
    pygame.time.delay(seconds*1000)


def get_player_default_pos(num=1):
    if num == 1:
        x = settings.PADDLE_OFFSET
    else:
        x = settings.WINDOW_WIDTH - (settings.PADDLE_THICKNESS + settings.PADDLE_OFFSET)

    y = (settings.WINDOW_HEIGHT - settings.PADDLE_SIZE) // 2
    return x, y


def get_ball_default_pos():
    x = (settings.WINDOW_WIDTH // 2) - (settings.LINE_THICKNESS // 2)
    y = (settings.WINDOW_HEIGHT // 2) - (settings.LINE_THICKNESS // 2)
    return x, y


def handle_ball_movement(ball_rect, dir_x, dir_y):
    if ball_rect.left < 0 or ball_rect.right > settings.WINDOW_WIDTH:
        ball_rect.move((-dir_x, dir_y))
    elif ball_rect.top < 0 or ball_rect.bottom > settings.WINDOW_HEIGHT:
        ball_rect.move((dir_x, -dir_y))
    else:
        ball_rect.move((dir_x, dir_y))


def handle_player_movement(player, ball_rect, ball_velocity):
    step = abs(settings.DEFAULT_SPEED)
    if ball_velocity[0] <= 0:
        if player.centery < settings.WINDOW_HEIGHT//2:
            player.y += step
        elif player.centery > settings.WINDOW_HEIGHT//2:
            player.y -= step
    else:
        if player.centery > ball_rect.centery:
            player.y -= step
        else:
            player.y += step
