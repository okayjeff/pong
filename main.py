import sys
import pygame

from pong import settings
from pong.models.announcement import Announcement
from pong.models.arena import Arena
from pong.models.ball import Ball
from pong.models.player import Player
from pong.models.scoreboard import Scoreboard
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
DISPLAY_SURF = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
)


def init():
    pygame.init()
    pygame.display.set_caption(settings.GAME_NAME)


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

    # Stack used to maintain render order
    game_objects = [
        arena,
        scoreboard,
        player_1,
        player_2,
        ball
    ]

    celebrating = False  # Are we celebrating a point?

    # Main loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                player_1.move((0, event.pos[1]-player_1.y))

        # Logic

        # If we're celebrating, then the Announcement object must be
        # on top of the stack.
        if celebrating:
            delay(2)
            game_objects.pop()
            celebrating = False

        if ball.hits_top_edge() or ball.hits_bottom_edge():
            ball.velocity[1] = -ball.velocity[1]

        if player_1.hits_ball(ball) or player_2.hits_ball(ball):
            ball.velocity[0] = -ball.velocity[0]

        scoring_player = check_point_scored(ball)
        if scoring_player:
            scoreboard.scores[scoring_player] += 1
            if check_for_winner(scoring_player, scores, settings.WINNING_SCORE):
                pygame.quit()
                sys.exit()

            celebrating = True
            announcement = Announcement(DISPLAY_SURF, 'Player {} scores!'.format(scoring_player))
            game_objects.append(announcement)

            ball.reposition(get_ball_default_pos())

        handle_ball_movement(ball, ball.velocity[0], ball.velocity[1])
        handle_player_movement(player_2, ball, ball.velocity)

        # Rendering
        render_game_objects(game_objects)
        pygame.display.update()
        FPS_CLOCK.tick(settings.FPS)


if __name__ == '__main__':
    main()
