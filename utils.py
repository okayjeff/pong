import sys

import pygame

from pong import settings


def pygame_init():
    pygame.init()
    pygame.display.set_caption(settings.GAME_NAME)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
    )
    return screen, clock


def check_point_scored(ball_rect):
    if ball_rect.left <= settings.LEFT_EDGE:
        return settings.PLAYER_TWO
    elif ball_rect.right >= settings.RIGHT_EDGE:
        return settings.PLAYER_ONE


def delay(seconds):
    pygame.time.delay(seconds*1000)


def exit_game():
    pygame.quit()
    sys.exit()


def get_ball_default_pos():
    x = (settings.WINDOW_WIDTH // 2) - (settings.LINE_THICKNESS // 2)
    y = (settings.WINDOW_HEIGHT // 2) - (settings.LINE_THICKNESS // 2)
    return x, y


def get_player_default_pos(num=1):
    if num == 1:
        x = settings.PADDLE_OFFSET
    else:
        x = settings.WINDOW_WIDTH - (settings.PADDLE_THICKNESS + settings.PADDLE_OFFSET)

    y = (settings.WINDOW_HEIGHT - settings.PADDLE_SIZE) // 2
    return x, y


def handle_ball_movement(ball, player_1, player_2):
    if ball.hits_top_edge() or ball.hits_bottom_edge():
        ball.velocity[1] = -ball.velocity[1]

    if player_1.hits_ball(ball) or player_2.hits_ball(ball):
        ball.velocity[0] = -ball.velocity[0]

    ball.move(ball.velocity)


def handle_player_movement(player, ball_rect, ball_velocity):
    step = abs(ball_velocity[0])
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


def render_game_objects(objs):
    for obj in objs:
        obj.render()
