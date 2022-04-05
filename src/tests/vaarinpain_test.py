import unittest
from vaarinpain import Vaarinpain
import pygame

class TestVaarinpain(unittest.TestCase):
    def setUp(self):
        print("This is setup")

    def test_to_print(self):
        self.assertEqual("ok", "ok")
