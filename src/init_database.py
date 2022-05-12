import sqlite3

for_ristinolla = sqlite3.connect("datafile/tilastot.db")
cursor = for_ristinolla.cursor()

cursor.execute(
    "CREATE TABLE Pelit (id INTEGER PRIMARY KEY, mode INTEGER, maara INTEGER);")
cursor.execute("INSERT INTO Pelit (mode, maara) VALUES (1, 0);")
cursor.execute("INSERT INTO Pelit (mode, maara) VALUES (2, 0);")
cursor.execute("INSERT INTO Pelit (mode, maara) VALUES (3, 0);")
for_ristinolla.commit()
