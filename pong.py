import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_WIDTH = 125
PADDLE_HEIGHT = 25

FLOOR = screen.get_height()-PADDLE_HEIGHT


def fill_surface(surface, color):
    surface.fill(color)


def draw_paddle(left, top, w, h):
    rect = pygame.Rect(left, top, w, h)
    return screen.fill(WHITE, rect)


paddle = draw_paddle(200, FLOOR, 125, 25)
last_pos = (200, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.fill(BLACK)
        if event.type == pygame.MOUSEMOTION:
            last_pos = (event.pos[0], event.pos[1])

    screen.fill(BLACK)
    draw_paddle(last_pos[0], FLOOR, 125, 25)
    pygame.display.flip()
