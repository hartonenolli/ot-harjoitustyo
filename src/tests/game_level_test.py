import unittest
from game_level import GameLevel


class TestGameLevel(unittest.TestCase):
    def setUp(self):
        self.level_map_1 = [[0, 2, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0]]

        self.cell_size = 200
        self.level_1 = GameLevel(self.level_map_1, self.cell_size)

        self.level_map_2 = [[2, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [2, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [3, 0, 1, 0, 0]]

        self.level_2 = GameLevel(self.level_map_2, self.cell_size)

        self.coordinates_1 = [[(0, 0), (200, 0), (400, 0), (600, 0), (800, 0)],
                              [(0, 200), (200, 200), (400, 200),
                               (600, 200), (800, 200)],
                              [(0, 400), (200, 400), (400, 400),
                               (600, 400), (800, 400)],
                              [(0, 600), (200, 600), (400, 600),
                               (600, 600), (800, 600)],
                              [(0, 800), (200, 800), (400, 800),
                               (600, 800), (800, 800)],
                              ]

    def test_start_True(self):
        self.assertTrue(GameLevel)

    def test_chek_loze_1(self):
        test_result = GameLevel.chek_loze(GameLevel, self.level_map_1)
        self.assertEqual(test_result, False)

    def test_chek_loze_2(self):
        test_result = GameLevel.chek_loze(GameLevel, self.level_map_2)
        self.assertEqual(test_result, True)

    def test_chek_loze_3(self):
        test_result = GameLevel.chek_loze(GameLevel, [[0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0],
                                                   [0, 1, 1, 1, 0],
                                                   [0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0]])
        self.assertEqual(test_result, True)

    def test_chek_loze_4(self):
        test_result = GameLevel.chek_loze(GameLevel, [[0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0],
                                                   [0, 2, 0, 0, 0],
                                                   [0, 0, 2, 0, 0],
                                                   [0, 0, 0, 2, 0]])
        self.assertEqual(test_result, True)

    def test_chek_loze_5(self):
        test_result = GameLevel.chek_loze(GameLevel, [[0, 0, 0, 0, 0],
                                                   [0, 0, 0, 1, 0],
                                                   [0, 0, 1, 2, 0],
                                                   [0, 1, 0, 0, 0],
                                                   [0, 0, 2, 0, 0]])
        self.assertEqual(test_result, True)

    def test_handle_click(self):
        test_result = GameLevel.handle_click(GameLevel,
                                             1, (100, 100), self.coordinates_1, self.level_map_1
                                    )
        self.assertEqual(test_result, [[1, 2, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 1, 0, 0]])

    def test_handle_click_2(self):
        test_result = GameLevel.handle_click(GameLevel,
                                             1, (100, 100), self.coordinates_1, self.level_map_2)
        self.assertEqual(test_result, False)
