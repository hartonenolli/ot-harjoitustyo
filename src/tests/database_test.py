from dataclasses import dataclass
import unittest
import sqlite3
from database_ristinolla import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.fake_data = "src/datatest/test_database.db"
        self.to_ristinolla = sqlite3.connect(self.fake_data)
        self.cursor = self.to_ristinolla.cursor()
        self.cursor.execute("UPDATE Pelit SET maara=0 WHERE mode<=3;")
        self.to_ristinolla.commit()

    def test_fech_amount_of_games_1(self):
        result = Database(self.fake_data).fech_amount_of_games(1)
        self.assertEqual(result, 0)

    def test_add_game_1(self):
        result = Database(self.fake_data).add_game(1)
        self.assertEqual(result, 1)

    def test_fech_amount_of_games_2(self):
        result = Database(self.fake_data).fech_amount_of_games(2)
        self.assertEqual(result, 0)

    def test_add_game_2(self):
        result = Database(self.fake_data).add_game(2)
        self.assertEqual(result, 1)

    def test_fech_amount_of_games_3(self):
        result = Database(self.fake_data).fech_amount_of_games(3)
        self.assertEqual(result, 0)

    def test_add_game_3(self):
        result = Database(self.fake_data).add_game(3)
        self.assertEqual(result, 1)

    def test_add_fech_amount_of_games_4(self):
        result = Database(self.fake_data).fech_amount_of_games(4)
        self.assertEqual(result, False)

    def test_add_game_4(self):
        result = Database(self.fake_data).add_game(4)
        self.assertEqual(result, False)

    def test_add_many_games_1(self):
        result = Database(self.fake_data).add_game(1)
        result += Database(self.fake_data).add_game(1)
        self.assertEqual(result, 3)

    def test_add_many_games_2(self):
        result = Database(self.fake_data).add_game(2)
        result += Database(self.fake_data).add_game(2)
        self.assertEqual(result, 3)

    def test_add_many_games_3(self):
        result = Database(self.fake_data).add_game(3)
        result += Database(self.fake_data).add_game(3)
        self.assertEqual(result, 3)

    def test_is_correct_1(self):
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).add_game(3)
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).add_game(1)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(1), 3)

    def test_is_correct_2(self):
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).add_game(3)
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).add_game(1)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(2), 1)

    def test_is_correct_3(self):
        Database(self.fake_data).add_game(3)
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).add_game(3)
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).add_game(1)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(3), 2)

    def test_fech_and_add_1(self):
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).fech_amount_of_games(2)
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).fech_amount_of_games(1)
        Database(self.fake_data).add_game(3)
        Database(self.fake_data).fech_amount_of_games(1)
        Database(self.fake_data).add_game(3)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(3), 2)

    def test_fech_and_add_2(self):
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).fech_amount_of_games(2)
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).fech_amount_of_games(2)
        Database(self.fake_data).add_game(2)
        Database(self.fake_data).fech_amount_of_games(4)
        Database(self.fake_data).add_game(3)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(2), 3)

    def test_fech_and_add_3(self):
        Database(self.fake_data).add_game(3)
        Database(self.fake_data).fech_amount_of_games(1)
        Database(self.fake_data).add_game(4)
        Database(self.fake_data).fech_amount_of_games(3)
        Database(self.fake_data).add_game(1)
        Database(self.fake_data).fech_amount_of_games(2)
        Database(self.fake_data).add_game(3)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(1), 1)

    def test_no_good_inputs_1(self):
        Database(self.fake_data).add_game(0)
        Database(self.fake_data).fech_amount_of_games(-1)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(True), False)

    def test_no_good_inputs_2(self):
        Database(self.fake_data).add_game(-2)
        Database(self.fake_data).add_game(64)
        Database(self.fake_data).fech_amount_of_games("b")
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(-2), False)

    def test_no_good_inputs_3(self):
        Database(self.fake_data).add_game(0.5)
        Database(self.fake_data).fech_amount_of_games(True)
        Database(self.fake_data).add_game(False)
        self.assertEqual(Database(self.fake_data).fech_amount_of_games("b"), False)

    def test_class(self):
        self.assertNotEqual(Database(self.fake_data), 0)

    def test_new_update_1(self):
        self.cursor.execute("UPDATE Pelit SET maara=10 WHERE mode=1;")
        self.to_ristinolla.commit()
        self.cursor.execute("UPDATE Pelit SET maara=10 WHERE mode=1;")
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(1), 10)

    def test_new_update_2(self):
        self.cursor.execute("UPDATE Pelit SET maara=100 WHERE mode=3;")
        self.cursor.execute("UPDATE Pelit SET maara=50 WHERE mode=2;")
        self.to_ristinolla.commit()
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(2), 50)

    def test_new_update_3(self):
        self.cursor.execute("UPDATE Pelit SET maara=100 WHERE mode=3;")
        self.to_ristinolla.commit()
        self.assertEqual(Database(self.fake_data).fech_amount_of_games(3), 100)
