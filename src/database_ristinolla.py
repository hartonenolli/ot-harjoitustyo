import sqlite3


class Database:
    def __init__(self, name_of_database):
        self.to_ristinolla = sqlite3.connect(name_of_database)
        self.cursor = self.to_ristinolla.cursor()

    def fech_amount_of_games(self, game_mode):
        if game_mode not in (1, 2, 3):
            return False
        amount = self.cursor.execute(
            "SELECT maara FROM Pelit where mode=?;", [game_mode]).fetchone()
        self.to_ristinolla.commit()
        return amount[0]

    def add_game(self, game_mode):
        if game_mode not in (1, 2, 3):
            return False
        total = self.fech_amount_of_games(game_mode)
        self.cursor.execute("UPDATE Pelit SET maara=? WHERE mode=?;", [
                            1+total, game_mode])

        amount = self.cursor.execute(
            "SELECT maara FROM Pelit where mode=?;", [game_mode]).fetchone()
        self.to_ristinolla.commit()
        return amount[0]
