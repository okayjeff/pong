import sys
import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

HALF_WINDOW_WIDTH = WINDOW_WIDTH // 2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT // 2

CENTER_LINE_THICKNESS = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_WIDTH = 125
PADDLE_HEIGHT = 25

FPS = 60
FPS_CLOCK = pygame.time.Clock()

DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_arena():
    DISPLAY_SURF.fill(BLACK)
    mid_top = (HALF_WINDOW_WIDTH, 0)
    mid_bottom = (HALF_WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.draw.line(
        DISPLAY_SURF,
        WHITE,
        mid_top,
        mid_bottom,
        CENTER_LINE_THICKNESS
    )


draw_arena()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
