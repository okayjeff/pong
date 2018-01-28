import sys
import pygame

from pong import settings
from pong.player import Player
from pong.settings import *
from pong.utils import delay


pygame.init()
pygame.display.set_caption(GAME_NAME)

FPS_CLOCK = pygame.time.Clock()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


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


def draw_ball(screen, ball_rect, color):
    pygame.draw.rect(screen, color, ball_rect)


def draw_scoreboard(screen, scores, font_size, color, position):
    font = pygame.font.SysFont('Hack', font_size)
    score_surf = font.render('{} {}'.format(scores[0], scores[1]), False, color)
    score_rect = score_surf.get_rect()
    score_rect.centerx, score_rect.y = position
    screen.blit(score_surf, score_rect)


def reset_ball(ball_rect):
    ball_rect.centerx = WINDOW_WIDTH // 2
    ball_rect.centery = WINDOW_HEIGHT // 2


def move_ball(ball_rect, dir_x, dir_y):
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        ball_rect.move_ip(-dir_x, dir_y)
    elif ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        ball_rect.move_ip(dir_x, -dir_y)
    else:
        ball_rect.move_ip(dir_x, dir_y)


def handle_player_movement(player, ball_rect, ball_velocity):
    step = abs(settings.DEFAULT_SPEED)
    if ball_velocity[0] <= 0:
        if player.centery < WINDOW_HEIGHT//2:
            player.y += step
        elif player.centery > WINDOW_HEIGHT//2:
            player.y -= step
    else:
        if player.centery > ball_rect.centery:
            player.y -= step
        else:
            player.y += step


def check_point_scored(ball_rect):
    if ball_rect.left <= LEFT_EDGE:
        scores[1] += 1
        return PLAYER_TWO
    elif ball_rect.right >= RIGHT_EDGE:
        scores[0] += 1
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


player_1 = Player('Player 1', DISPLAY_SURF, settings)
player_2 = Player('Player 2', DISPLAY_SURF, settings, cpu=True)

ball_x = (WINDOW_WIDTH // 2) - (LINE_THICKNESS // 2)
ball_y = (WINDOW_HEIGHT // 2) - (LINE_THICKNESS // 2)
ball = pygame.Rect(ball_x, ball_y, BALL_THICKNESS, BALL_THICKNESS)

ball_velocity = [DEFAULT_SPEED, DEFAULT_SPEED]

scores = [0, 0]


draw_arena()
player_1.render()
player_2.render()
draw_ball(DISPLAY_SURF, ball, WHITE)
draw_scoreboard(DISPLAY_SURF, scores, SCOREBOARD_FONT_SIZE, WHITE, MID_TOP)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEMOTION:
            player_1.move((0, event.pos[1]-player_1.y))

    if ball.top < TOP_EDGE or ball.bottom > BOTTOM_EDGE:
        ball_velocity[1] = -ball_velocity[1]

    if player_1.rect.colliderect(ball) or player_2.rect.colliderect(ball):
        ball_velocity[0] = -ball_velocity[0]

    scoring_player = check_point_scored(ball)
    if scoring_player:
        if check_for_winner(scoring_player, scores, WINNING_SCORE):
            celebrate_game_winner(scoring_player)
            pygame.quit()
            sys.exit()
        celebrate_point_scored(scoring_player, DISPLAY_SURF, SCOREBOARD_FONT_SIZE, WHITE, DEAD_CENTER)
        reset_ball(ball)
        delay(3)

    move_ball(ball, ball_velocity[0], ball_velocity[1])
    handle_player_movement(player_2, ball, ball_velocity)

    draw_arena()
    player_1.render()
    player_2.render()
    draw_ball(DISPLAY_SURF, ball, WHITE)
    draw_scoreboard(DISPLAY_SURF, scores, SCOREBOARD_FONT_SIZE, WHITE, MID_TOP)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
