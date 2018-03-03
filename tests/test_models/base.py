import unittest

from models.ball import Ball


class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()
