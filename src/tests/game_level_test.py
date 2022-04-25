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

        self.coordinates_1 = [[(0,0),(200,0),(400,0),(600,0),(800,0)],
                        [(0,200),(200,200),(400,200),(600,200),(800,200)],
                        [(0,400),(200,400),(400,400),(600,400),(800,400)],
                        [(0,600),(200,600),(400,600),(600,600),(800,600)],
                        [(0,800),(200,800),(400,800),(600,800),(800,800)],
                        ]

    def test_start_True(self):
        self.assertTrue(GameLevel)

    def test_c_loze_1(self):
        test_result =GameLevel.c_loze(self.LEVEL_MAP_1)
        self.assertEqual(test_result, False)

    def test_c_loze_2(self):
        test_result =GameLevel.c_loze(self.LEVEL_MAP_2)
        self.assertEqual(test_result, True)

    def test_handle_click(self):
        test_result = GameLevel.handle_click(1, (100,100), self.coordinates_1, self.LEVEL_MAP_1)
        self.assertEqual(test_result, [[1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])
