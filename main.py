import pygame

from pong import settings
from pong.models.arena import Arena
from pong.models.ball import Ball
from pong.models.clock import Clock
from pong.models.player import Player
from pong.models.screens import show_game_over_screen, show_title_screen
from pong.utils.helpers import (
    pygame_init,
    check_point_scored,
    exit_game,
    get_ball_default_pos,
    get_player_default_pos,
    handle_ball_movement,
    handle_player_movement,
    render_game_objects,
)


DISPLAY_SURF, FPS_CLOCK = pygame_init()


def main():
    difficulty = settings.EASY
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
        velocity=[difficulty, difficulty]
    )

    clock = Clock(surf=DISPLAY_SURF)
    clock.start()

    # Stack used to maintain render order
    game_objects = [
        arena,
        player_1,
        player_2,
        ball,
        clock,
    ]

    # Main loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            elif event.type == pygame.MOUSEMOTION:
                player_1.move((0, event.pos[1]-player_1.y))

        # Logic
        game_over = check_point_scored(ball)
        if game_over:
            clock.stop()
            elapsed = clock.get_elapsed_seconds()
            show_game_over_screen(DISPLAY_SURF, FPS_CLOCK, elapsed)
            clock.reset()
            clock.start()

            ball.reset_velocity()
            ball.reposition(get_ball_default_pos())

        handle_ball_movement(ball, player_1, player_2)
        handle_player_movement(player_2, ball, ball.velocity)

        # Rendering
        render_game_objects(game_objects)
        pygame.display.update()
        FPS_CLOCK.tick(settings.FPS)


if __name__ == '__main__':
    show_title_screen(DISPLAY_SURF, FPS_CLOCK)
    main()
