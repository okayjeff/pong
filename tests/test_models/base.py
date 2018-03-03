import pygame
import unittest

import settings


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.display_surface = pygame.Surface(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        self.default_pos = (0, 0)
