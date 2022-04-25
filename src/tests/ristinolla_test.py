import unittest
from ristinolla import Ristinolla
from game_level import GameLevel

class TestRistinolla(unittest.TestCase):
    def setUp(self):
        pass

    def test_start_True(self):
        self.assertTrue(Ristinolla)
