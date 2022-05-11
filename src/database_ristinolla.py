import sqlite3

class Database:
    def __init__(self):
        self.to_ristinolla = sqlite3.connect("src/tilastot.db")
        self.cursor = self.to_ristinolla.cursor()

    def fech_amount_of_games(self):
        amount = self.cursor.execute("SELECT maara FROM Pelit").fetchone()
        self.to_ristinolla.commit()
        return amount[0]

    def add_game(self):
        total = self.fech_amount_of_games()
        self.cursor.execute("UPDATE Pelit SET maara=?;",[1+total])
        self.to_ristinolla.commit()
