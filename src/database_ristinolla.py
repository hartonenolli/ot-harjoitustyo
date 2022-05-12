import sqlite3


class Database:
    def __init__(self):
        self.to_ristinolla = sqlite3.connect("datafile/tilastot.db")
        self.cursor = self.to_ristinolla.cursor()

    def fech_amount_of_games(self, game_mode):
        amount = self.cursor.execute(
            "SELECT maara FROM Pelit where mode=?;", [game_mode]).fetchone()
        self.to_ristinolla.commit()
        return amount[0]

    def add_game(self, game_mode):
        total = self.fech_amount_of_games(game_mode)
        self.cursor.execute("UPDATE Pelit SET maara=? WHERE mode=?;", [
                            1+total, game_mode])
        self.to_ristinolla.commit()
