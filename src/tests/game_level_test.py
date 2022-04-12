import unittest
from game_level import GameLevel




class TestGameLevel(unittest.TestCase):
    def setUp(self):
        self.LEVEL_MAP_1 = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

        self.CELL_SIZE = 200
        self.level_1 = GameLevel(self.LEVEL_MAP_1, self.CELL_SIZE)

        self.LEVEL_MAP_2 = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]]

        self.level_2 = GameLevel(self.LEVEL_MAP_2, self.CELL_SIZE)


    def test_start_True(self):
        self.assertTrue(GameLevel)

    def test_c_loze_1(self):
        test_result =GameLevel.c_loze(self.LEVEL_MAP_1)
        self.assertEqual(test_result, False)

    def test_c_loze_2(self):
        test_result =GameLevel.c_loze(self.LEVEL_MAP_2)
        self.assertEqual(test_result, True)