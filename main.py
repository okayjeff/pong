import sys
import pygame

from pong import settings
from pong.models.ball import Ball
from pong.models.player import Player
from pong.settings import *
from pong.utils import (
    delay,
    get_ball_default_pos,
    get_player_default_pos,
    handle_ball_movement,
    handle_player_movement,
    render_game_objects
)


FPS_CLOCK = pygame.time.Clock()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def init():
    pygame.init()
    pygame.display.set_caption(GAME_NAME)


def draw_arena():
    DISPLAY_SURF.fill(BLACK)
    mid_top = (HALF_WINDOW_WIDTH, 0)
    mid_bottom = (HALF_WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.draw.rect(DISPLAY_SURF, WHITE, ((0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), ARENA_BORDER_THICKNESS)
    pygame.draw.line(
        DISPLAY_SURF,
        WHITE,
        mid_top,
        mid_bottom,
        LINE_THICKNESS//4
    )


def draw_scoreboard(screen, scores, font_size, color, position):
    font = pygame.font.SysFont('Hack', font_size)
    p1_score = scores[settings.PLAYER_ONE]
    p2_score = scores[settings.PLAYER_TWO]
    score_surf = font.render('{} {}'.format(p1_score, p2_score), False, color)
    score_rect = score_surf.get_rect()
    score_rect.centerx, score_rect.y = position
    screen.blit(score_surf, score_rect)


def check_point_scored(ball_rect, scores):
    if ball_rect.left <= LEFT_EDGE:
        return PLAYER_TWO
    elif ball_rect.right >= RIGHT_EDGE:
        return PLAYER_ONE


def check_for_winner(player, scores, winning_pts):
    player_score_idx = player - 1
    player_pts = scores[player_score_idx]
    if player_pts >= winning_pts:
        return player


def celebrate_point_scored(player, screen, font_size, text_color, pos, bg_color=None):
    pname = 'Player One' if player == 1 else 'Player Two'
    text = '{} scored!'.format(pname)

    font = pygame.font.SysFont('Hack', font_size)
    celeb_surf = font.render(text, False, text_color, bg_color)
    celeb_rect = celeb_surf.get_rect()
    celeb_rect.centerx, celeb_rect.centery = pos
    screen.blit(celeb_surf, celeb_rect)


def celebrate_game_winner(player):
    pass


def main():
    init()

    player_1 = Player(
        name=settings.PLAYER_ONE,
        surf=DISPLAY_SURF,
        pos=get_player_default_pos()
    )

    player_2 = Player(
        name=settings.PLAYER_TWO,
        surf=DISPLAY_SURF,
        pos=get_player_default_pos(num=settings.PLAYER_TWO)
    )

    ball = Ball(
        surf=DISPLAY_SURF,
        pos=get_ball_default_pos(),
        velocity=[settings.DEFAULT_SPEED, settings.DEFAULT_SPEED]
    )

    scores = {
        settings.PLAYER_ONE: 0,
        settings.PLAYER_TWO: 0
    }

    draw_arena()
    render_game_objects(player_1, player_2, ball)
    draw_scoreboard(DISPLAY_SURF, scores, SCOREBOARD_FONT_SIZE, WHITE, MID_TOP)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                player_1.move((0, event.pos[1]-player_1.y))

        if ball.top < TOP_EDGE or ball.bottom > BOTTOM_EDGE:
            ball.velocity[1] = -ball.velocity[1]

        if player_1.rect.colliderect(ball) or player_2.rect.colliderect(ball):
            ball.velocity[0] = -ball.velocity[0]

        scoring_player = check_point_scored(ball, scores)
        if scoring_player:
            scores[scoring_player] += 1
            if check_for_winner(scoring_player, scores, WINNING_SCORE):
                celebrate_game_winner(scoring_player)
                pygame.quit()
                sys.exit()
            celebrate_point_scored(scoring_player, DISPLAY_SURF, SCOREBOARD_FONT_SIZE, WHITE, DEAD_CENTER)
            ball.reposition(get_ball_default_pos())
            delay(3)

        handle_ball_movement(ball, ball.velocity[0], ball.velocity[1])
        handle_player_movement(player_2, ball, ball.velocity)

        draw_arena()
        render_game_objects(player_1, player_2, ball)
        draw_scoreboard(DISPLAY_SURF, scores, SCOREBOARD_FONT_SIZE, WHITE, MID_TOP)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    main()