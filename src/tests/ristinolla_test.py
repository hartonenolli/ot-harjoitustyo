import unittest
from ristinolla import Ristinolla
from game_level import GameLevel

class TestRistinolla(unittest.TestCase):
    def setUp(self):
        pass

    def test_start_True(self):
        self.assertTrue(Ristinolla)

LEVEL_MAP_1 = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

CELL_SIZE = 200


class TestGameLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = GameLevel(LEVEL_MAP_1)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)