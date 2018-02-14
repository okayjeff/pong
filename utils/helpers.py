import sys
import time

import pygame

import settings
from models.sounds import SoundController


def pygame_init():
    """
    Initialize pygame and return core pygame elements.

    Returns the main display surface along with the game clock object.
    """
    pygame.init()
    pygame.display.set_caption(settings.GAME_NAME)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
    )
    return screen, clock


def delay(seconds):
    pygame.time.delay(seconds*1000)


def exit_game():
    pygame.quit()
    records.exit()


def check_point_scored(ball_rect):
    """
    Checks if a point was scored by either player.
    """
    if ball_rect.left <= settings.LEFT_EDGE:
        return settings.PLAYER_TWO
    elif ball_rect.right >= settings.RIGHT_EDGE:
        return settings.PLAYER_ONE


def get_ball_default_pos():
    """
    Returns x, y coordinates for where the ball should be at the start of
    the game.
    """
    return settings.DEAD_CENTER


def get_player_default_pos(num=1):
    """
    Return default player position based on which player we're talking about.

    :param num: Player number, either 1 or 2, where 2 is the CPU.
    """
    if num == 1:
        x = settings.PADDLE_OFFSET
    else:
        x = settings.WINDOW_WIDTH - (settings.PADDLE_THICKNESS + settings.PADDLE_OFFSET)

    y = (settings.WINDOW_HEIGHT - settings.PADDLE_SIZE) // 2
    return x, y


def handle_ball_movement(ball, player_1, player_2):
    """
    Move the ball, bounce it off walls, and make it go faster each
    time player 1 successfully volleys it.
    """
    if ball.hits_top_edge() or ball.hits_bottom_edge():
        SoundController.play_thud()
        ball.velocity[1] = -ball.velocity[1]

    if player_1.hits_ball(ball) or player_2.hits_ball(ball):
        SoundController.play_racquet()
        ball.velocity[0] = -ball.velocity[0]

        # Every time player 1 hits ball increase speed
        # The ball will always be moving back toward player 2 at this point,
        # but the ball may be moving up/down, so need to account for that when
        # incrementing y velocity.
        if player_1.hits_ball(ball):
            ball.velocity[0] += 1
            if ball.velocity[1] < 0:
                ball.velocity[1] -= 1
            else:
                ball.velocity[1] += 1

    ball.move(ball.velocity)


def handle_player_movement(player, ball):
    """
    Automate cpu player movement.
    """
    step = abs(ball.velocity[0])
    mid_arena = settings.WINDOW_HEIGHT//2
    distance_from_mid_arena = abs(player.centery - mid_arena)

    if ball.is_moving_left():
        # If player distance from mid arena is less than step, just move player
        # to mid arena to avoid stuttering caused when moving position by
        # <step> pixels causes player to move too far up/down.
        if distance_from_mid_arena < step:
            player.centery = mid_arena
        elif player.centery < mid_arena:
            player.y += step
        elif player.centery > mid_arena:
            player.y -= step
    else:
        if player.centery > ball.centery:
            player.y -= step
        else:
            player.y += step


def render_game_objects(objs):
    """
    A helper to render a list of objects.
    """
    for obj in objs:
        obj.render()


def format_time(seconds):
    fmt = settings.TIME_FORMAT
    return time.strftime(fmt, time.gmtime(seconds))
