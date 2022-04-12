import unittest
from vaarinpain import Vaarinpain

class TestVaarinpain(unittest.TestCase):
    def setUp(self):
        pass

    def test_to_print(self):
        self.assertEqual("ok", "ok")

    def test_start_True(self):
        self.assertTrue(Vaarinpain)

    def test_start_screen(self):
        self.assertTrue(Vaarinpain.start_screen)

    def test_instructions(self):
        self.assertTrue(Vaarinpain.instructions)

    def test_game_mode(self):
        self.assertTrue(Vaarinpain.game_mode)
            
    def test_start_again(self):
        self.assertTrue(Vaarinpain.start_again)

    def test_play_setup(self):
        self.assertTrue(Vaarinpain.play_setup)
