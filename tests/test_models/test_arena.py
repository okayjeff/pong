import mock

from models.arena import Arena
from tests.test_models.base import ModelTestCase


class ArenaTestCase(ModelTestCase):

    def setUp(self):
        super(ArenaTestCase, self).setUp()
        self.arena = Arena(surf=self.display_surface)

    @mock.patch('models.arena.Arena._fill_background')
    @mock.patch('models.arena.Arena._draw_border')
    @mock.patch('models.arena.Arena._draw_center_line')
    def test_render(self, draw_line, draw_border, fill_bg):
        self.arena.render()
        methods = [draw_line, draw_border, fill_bg]
        for method in methods:
            self.assertTrue(method.called)
