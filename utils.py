import sys
import time

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

        # Every time player 1 hits ball increase speed
        if player_1.hits_ball(ball):
            if ball.velocity[0] < 0:
                ball.velocity[0] -= 1
            else:
                ball.velocity[0] += 1

            if ball.velocity[1] < 0:
                ball.velocity[1] -= 1
            else:
                ball.velocity[1] += 1

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


def get_records(fname=settings.RECORDS_FILENAME):
    """
    Open records file and return list of records.
    """
    try:
        with open(fname, 'r+') as f:
            records = [int(r) for r in f.readlines()]
    except FileNotFoundError:
        with open(fname, 'w+') as f:
            records = []
    return records


def get_formatted_records(fname=settings.RECORDS_FILENAME):
    records = [format_time(int(r)) for r in get_records(fname)]
    return records


def save_records_to_file(seconds, fname=settings.RECORDS_FILENAME):
    """
    Add given time in seconds to the records file.
    """
    records = get_records()
    record_time, idx = recent_time_is_record(seconds, records)
    if record_time:
        records = update_records(idx, seconds, records)
        with open(fname, 'w+') as f:
            for record in records:
                f.write('{}\n'.format(record))


def recent_time_is_record(seconds, records):
    """
    Return True if the given time in seconds is in the top 5
    saved on file.
    """
    if len(records) < 1:
        return True, 0
    for idx, record in enumerate(records):
        if int(seconds) > int(record):
            return True, idx
    return False, None


def update_records(idx, seconds, records):
    records.insert(idx, seconds)
    if len(records) > 5:
        records.pop()
    return records


def format_time(seconds):
    fmt = settings.TIME_FORMAT
    return time.strftime(fmt, time.gmtime(seconds))
