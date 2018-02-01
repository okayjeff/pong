import pygame

from pong import settings
from pong.models.announcement import Announcement
from pong.models.arena import Arena
from pong.models.ball import Ball
from pong.models.player import Player
from pong.models.scoreboard import Scoreboard
from pong.models.screens import ModalScreen
from pong.utils import (
    pygame_init,
    check_for_winner,
    check_point_scored,
    delay,
    exit_game,
    get_ball_default_pos,
    get_player_default_pos,
    handle_ball_movement,
    handle_player_movement,
    render_game_objects
)


DISPLAY_SURF, FPS_CLOCK = pygame_init()


def show_title_screen():
    title_screen = ModalScreen(
        surf=DISPLAY_SURF,
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
        FPS_CLOCK.tick(15)


def show_game_over_screen(player):
    game_over_screen = ModalScreen(
        surf=DISPLAY_SURF,
        title_text='Player {} wins!'.format(player),
        subtitle_text='Press the SPACE bar to play again.'
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
        FPS_CLOCK.tick(15)


def show_point_scored_message(player):
    announcement = Announcement(DISPLAY_SURF, 'Player {} scores!'.format(player))
    show = True
    start = pygame.time.get_ticks()
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        now = pygame.time.get_ticks()
        if now-start > 2000:
            show = False

        announcement.render()
        pygame.display.update()
        FPS_CLOCK.tick(15)


def main():
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

    # Main loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            elif event.type == pygame.MOUSEMOTION:
                player_1.move((0, event.pos[1]-player_1.y))

        # Logic

        if ball.hits_top_edge() or ball.hits_bottom_edge():
            ball.velocity[1] = -ball.velocity[1]

        if player_1.hits_ball(ball) or player_2.hits_ball(ball):
            ball.velocity[0] = -ball.velocity[0]

        scoring_player = check_point_scored(ball)
        if scoring_player:
            scoreboard.scores[scoring_player] += 1
            show_point_scored_message(scoring_player)

            if check_for_winner(scoring_player, scores):
                show_game_over_screen(scoring_player)

            ball.reposition(get_ball_default_pos())

        handle_ball_movement(ball, ball.velocity[0], ball.velocity[1])
        handle_player_movement(player_2, ball, ball.velocity)

        # Rendering
        render_game_objects(game_objects)
        pygame.display.update()
        FPS_CLOCK.tick(settings.FPS)


if __name__ == '__main__':
    show_title_screen()
    main()
