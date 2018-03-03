import mock

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

    def test_reset_velocity_sets_to_default_speed(self):
        self.ball.velocity = (200, 200)
        self.ball.reset_velocity()
        default_velocity = [settings.DEFAULT_SPEED, settings.DEFAULT_SPEED]
        self.assertEqual(self.ball.velocity, default_velocity)

    def test_is_moving_left_when_velocity_x_less_than_zero(self):
        self.ball.velocity[0] = -1
        self.assertTrue(self.ball.is_moving_left())

    def test_not_moving_left_when_velocity_x_zero_or_greater(self):
        self.ball.velocity[0] = 0
        self.assertFalse(self.ball.is_moving_left())

        self.ball.velocity[0] = 1
        self.assertFalse(self.ball.is_moving_left())

    def test_is_moving_left_after_velocity_reset(self):
        self.ball.reset_velocity()
        self.assertTrue(self.ball.is_moving_left())

    def test_is_moving_right_when_velocity_x_greater_than_zero(self):
        self.ball.velocity[0] = 1
        self.assertTrue(self.ball.is_moving_right())

    def test_not_moving_right_when_velocity_x_less_than_zero(self):
        self.ball.velocity[0] = 0
        self.assertFalse(self.ball.is_moving_right())

        self.ball.velocity[0] = -1
        self.assertFalse(self.ball.is_moving_right())

    @mock.patch('pygame.draw.rect')
    def test_render_draws_rectangle(self, mock_draw):
        self.ball.render()
        mock_draw.assert_called_with(
            self.ball.surf,
            self.ball.color,
            self.ball.rect
        )
