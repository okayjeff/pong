import sys
import pygame

from pong import settings
from pong.models.arena import Arena
from pong.models.ball import Ball
from pong.models.player import Player
from pong.models.scoreboard import Scoreboard
from pong.settings import *
from pong.utils import (
    check_for_winner,
    check_point_scored,
    delay,
    get_ball_default_pos,
    get_player_default_pos,
    handle_ball_movement,
    handle_player_movement,
    render_game_objects
)


FPS_CLOCK = pygame.time.Clock()
DISPLAY_SURF = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))


def init():
    pygame.init()
    pygame.display.set_caption(settings.GAME_NAME)


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

    arena = Arena(surf=DISPLAY_SURF)

    player_1 = Player(
        name=settings.PLAYER_ONE,
        surf=DISPLAY_SURF,
        pos=get_player_default_pos(num=settings.PLAYER_ONE)
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

    scoreboard = Scoreboard(
        surf=DISPLAY_SURF,
        pos=settings.MID_TOP,
        scores=scores
    )

    render_game_objects(arena, scoreboard, player_1, player_2, ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                player_1.move((0, event.pos[1]-player_1.y))

        if ball.hits_top_edge() or ball.hits_bottom_edge():
            ball.velocity[1] = -ball.velocity[1]

        if player_1.hits_ball(ball) or player_2.hits_ball(ball):
            ball.velocity[0] = -ball.velocity[0]

        scoring_player = check_point_scored(ball)
        if scoring_player:
            scoreboard.scores[scoring_player] += 1
            if check_for_winner(scoring_player, scores, WINNING_SCORE):
                celebrate_game_winner(scoring_player)
                pygame.quit()
                sys.exit()
            celebrate_point_scored(scoring_player, DISPLAY_SURF, SCOREBOARD_FONT_SIZE, WHITE, DEAD_CENTER)
            ball.reposition(get_ball_default_pos())
            delay(3)

        handle_ball_movement(ball, ball.velocity[0], ball.velocity[1])
        handle_player_movement(player_2, ball, ball.velocity)

        render_game_objects(arena, scoreboard, player_1, player_2, ball)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
