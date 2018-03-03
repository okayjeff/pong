import settings
from models.ball import Ball
from tests.test_models.base import ModelTestCase


class BallTestCase(ModelTestCase):
    def setUp(self):
        super(BallTestCase, self).setUp()
        self.ball = Ball(
            surf=self.display_surface,
            pos=self.default_pos,
            speed=settings.DEFAULT_SPEED
        )

    def test_hits_top_edge_returns_true(self):
        self.ball.top = settings.TOP_EDGE
        self.assertTrue(self.ball.hits_top_edge())

    def test_hits_top_edge_returns_false(self):
        self.ball.top = settings.TOP_EDGE + 1
        self.assertFalse(self.ball.hits_top_edge())

    def test_hits_bottom_edge_returns_true(self):
        self.ball.bottom = settings.BOTTOM_EDGE
        self.assertTrue(self.ball.hits_bottom_edge())

    def test_hits_bottom_edge_returns_false(self):
        self.ball.bottom = settings.BOTTOM_EDGE - 1
        self.assertFalse(self.ball.hits_bottom_edge())
