import sys
import pygame

pygame.init()
pygame.display.set_caption('Pong')

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

HALF_WINDOW_WIDTH = WINDOW_WIDTH // 2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT // 2

LINE_THICKNESS = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_SIZE = 50
PADDLE_OFFSET = 20

FPS = 60
FPS_CLOCK = pygame.time.Clock()

DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

DEFAULT_SPEED = -2


def draw_arena():
    DISPLAY_SURF.fill(BLACK)
    mid_top = (HALF_WINDOW_WIDTH, 0)
    mid_bottom = (HALF_WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.draw.rect(DISPLAY_SURF, WHITE, ((0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), LINE_THICKNESS*2)
    pygame.draw.line(
        DISPLAY_SURF,
        WHITE,
        mid_top,
        mid_bottom,
        LINE_THICKNESS//4
    )


def draw_paddle(paddle_rect):
    # Stops paddle moving too low
    if paddle_rect.bottom > WINDOW_HEIGHT - LINE_THICKNESS:
        paddle_rect.bottom = WINDOW_HEIGHT - LINE_THICKNESS

    # Stops paddle moving too high
    elif paddle_rect.top < LINE_THICKNESS:
        paddle_rect.top = LINE_THICKNESS

    # Draws paddle
    pygame.draw.rect(DISPLAY_SURF, WHITE, paddle_rect)


def draw_ball(ball_rect):
    pygame.draw.rect(DISPLAY_SURF, WHITE, ball_rect)


def move_ball(ball_rect, dir_x, dir_y):
    if ball_rect.left < 0 or ball_rect.right > WINDOW_WIDTH:
        ball_rect.move_ip(-dir_x, dir_y)
    elif ball_rect.top < 0 or ball_rect.bottom > WINDOW_HEIGHT:
        ball_rect.move_ip(dir_x, -dir_y)
    else:
        ball_rect.move_ip(dir_x, dir_y)


player_one_pos = player_two_pos = (WINDOW_HEIGHT - PADDLE_SIZE) // 2
player_one = pygame.Rect(PADDLE_OFFSET, player_one_pos, LINE_THICKNESS*2, PADDLE_SIZE)
player_two = pygame.Rect(WINDOW_WIDTH-(PADDLE_OFFSET+LINE_THICKNESS*2), player_two_pos, LINE_THICKNESS*2, PADDLE_SIZE)

ball_x = (WINDOW_WIDTH // 2) - (LINE_THICKNESS // 2)
ball_y = (WINDOW_HEIGHT // 2) - (LINE_THICKNESS // 2)
ball = pygame.Rect(ball_x, ball_y, LINE_THICKNESS, LINE_THICKNESS)

ball_velocity = [DEFAULT_SPEED, DEFAULT_SPEED]


draw_arena()
draw_paddle(player_one)
draw_paddle(player_two)
draw_ball(ball)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ball.top < LINE_THICKNESS or ball.bottom > WINDOW_HEIGHT-LINE_THICKNESS:
        ball_velocity[1] = -ball_velocity[1]

    if player_one.colliderect(ball) or player_two.colliderect(ball):
        ball_velocity[0] = -ball_velocity[0]

    move_ball(ball, ball_velocity[0], ball_velocity[1])

    draw_arena()
    player_one.y = pygame.mouse.get_pos()[1]
    draw_paddle(player_one)
    draw_paddle(player_two)
    draw_ball(ball)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
